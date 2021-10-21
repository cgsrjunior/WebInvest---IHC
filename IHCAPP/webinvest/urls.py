from django.urls import path

from webinvest import goals_views
from webinvest import sing_views
from webinvest import statistic_view

from . import record_views

app_name = 'webinvest'
urlpatterns = [
    path('', sing_views.initial, name='initial'),
    path('record/', record_views.show_records, name='record'),
    path('record/<int:record_id>/delete/', record_views.delete, name='delete'),
    path('record/add/', record_views.add, name='record_add'),
    path('record/<int:record_id>/edit/', record_views.edit, name='edit'),

    path('goals/', goals_views.show_goals, name='goals'),

    path('singup/', sing_views.singup, name='singup'),
    path('user/', sing_views.user, name='user'),
    path('user/edit', sing_views.edit_user, name='user_edit'),

    path('statistics/', statistic_view.show_statistics, name='statistics'),

    path('initial', sing_views.initial, name='initial'),
]