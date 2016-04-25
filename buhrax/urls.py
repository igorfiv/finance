from django.conf.urls import url
from django.contrib.auth import views as auth_views


from . import views

app_name = 'buhrax'

urlpatterns = [
    url(r'^cash/$',
        views.cash_list, name='cash_list'),
    url(r'^planned/$',
        views.cash_planned_list, name='cash_planned_list'),
    url(r'^planned/add/$',
        views.planned_cash_create, name='planned_cash_create'),
    url(r'^planned/update/(?P<pk>[0-9]+)$',
        views.planned_cash_update, name='planned_cash_update'),
    url(r'^planned/delete/(?P<pk>[0-9]+)$',
        views.planned_cash_delete, name='planned_cash_delete'),
    url(r'^update/(?P<pk>[0-9]+)$',
        views.cash_update, name='cash_update'),
    url(r'^add/$',
        views.cash_create, name='cash_create'),
    url(r'^delete/(?P<pk>[0-9]+)$',
        views.cash_delete, name='cash_delete'),
    url(r'^finance_report/$',
        views.finance_report, name='finance_report'),
    url(r'^register/',
        views.register, name='register'),
    url(r'^accounts/login/$',
        auth_views.login, name='login'),
    url(r'^accounts/profile/$',
        views.user_profile, name='user_profile'),
    url(r'^logout/$',
        views.user_logout, name='user_logout'),
]
