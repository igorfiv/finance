from django.conf.urls import url
from django.contrib.auth import views as auth_views


from . import views

app_name = 'buhrax'

urlpatterns = [
    url(r'^cash/$',
        views.cash_list, name='cash_list'),
    url(r'^planned/$',
        views.cash_planned_list, name='cash_planned_list'),
    url(r'^update/(?P<pk>[0-9]+)$',
        views.cash_update, name='cash_update'),
    url(r'^add/$',
        views.cash_create, name='cash_create'),
    url(r'^delete/(?P<pk>[0-9]+)$',
        views.cash_delete, name='cash_delete'),
    url(r'^register/',
        views.register, name='register'),
    url(r'^accounts/login/$',
        auth_views.login, name='login'),
    url(r'^accounts/profile/$',
        views.user_profile, name='user_profile'),
    url(r'^logout/$',
        views.user_logout, name='user_logout'),
]
