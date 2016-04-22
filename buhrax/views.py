from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from .models import cash, UserProfile, cash_planned
from django.forms import ModelForm, Select, DateInput, TextInput
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


# Create your views here.

# Forms

class CashForm(ModelForm):
    class Meta:
        model = cash
        fields = ['cash_expense', 'cash_date',
                  'cash_type', 'cash_value', 'cash_desc'
                  ]
        widgets = {
            'cash_expense': Select(attrs={'class': 'form-control'}),
            'cash_date': DateInput(attrs={'class': 'form-control'}),
            'cash_type': Select(attrs={'class': 'form-control'}),
            'cash_value': TextInput(attrs={'class': 'form-control'}),
            'cash_desc': TextInput(attrs={'class': 'form-control'}),
        }

class CashPlannedFrom(ModelForm):
    class Meta:
        model = cash_planned
        fields = ['planned_cash_date', 'planned_cash_value',
                  'planned_cash_repeat','planned_cash_desc'
                  ]


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


# auth views

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    output = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}

    return render(request, 'registration/register.html', output)


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('buhrax:cash_list')
            else:
                return HttpResponse("Your account is disabled")
        else:
            print "Invalid credentials: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'registration/login.html', {})


def user_logout(request):
    logout(request)
    return redirect('buhrax:cash_list')


@login_required
def user_profile(request):
    return redirect('buhrax:cash_list')

# cash views


@login_required
def cash_list(request):
    cash_data = cash.objects.all()
    cash_total_r = cash.objects.filter(
        cash_type="R").aggregate(Sum('cash_value'))
    cash_total_p = cash.objects.filter(
        cash_type="P").aggregate(Sum('cash_value'))
    cash_total_z = cash.objects.filter(
        cash_type="Z").aggregate(Sum('cash_value'))

    cash_total = cash_total_p.get(
        'cash_value__sum') - cash_total_r.get('cash_value__sum')

    output = {'cash_data': cash_data,
              'cash_total': cash_total,
              'cash_total_p': cash_total_p,
              'cash_total_r': cash_total_r,
              'cash_total_z': cash_total_z
              }
    return render(request, 'cash.html', output)


@login_required
def cash_create(request):
    form = CashForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('buhrax:cash_list')

    return render(request, 'edit.html', {'form': form})


@login_required
def cash_update(request, pk):
    cash_record = get_object_or_404(cash, pk=pk)
    form = CashForm(request.POST or None, instance=cash_record)
    if form.is_valid():
        form.save()
        return redirect('buhrax:cash_list')

    return render(request, 'edit.html', {'form': form})


@login_required
def cash_delete(request, pk):
    cash_record = get_object_or_404(cash, pk=pk)
    if request.method == 'POST':
        cash_record.delete()
        return redirect('buhrax:cash_list')

    return render(request, 'delete.html', {'object': cash_record})

# planned cash views


@login_required
def cash_planned_list(request):
    planned_cash_data = planned_cash.objects.all()
    planned_cash_total = planned_cash.objects.aggregate(Sum('planned_cash_value'))

    output = {'planned_cash_data': planned_cash_data,
              'planned_cash_total': planned_cash_total
              }

    return render(request, 'planned.html', output)
