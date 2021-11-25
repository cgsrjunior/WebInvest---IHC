from django.urls import path

from webinvest import goals_views
from webinvest import sing_views
from webinvest import statistic_view
from webinvest import record_views

app_name = 'webinvest'
urlpatterns = [
    path('', sing_views.initial, name='initial'),
    path('record/', record_views.show_records, name='record'),
    path('record/<str:column_name>/<str:order>', record_views.show_records, name='record'),

    path('record/delete/<int:record_id>/', record_views.delete, name='delete'),
    path('record/add/', record_views.add, name='record_add'),
    path('record/edit/<int:record_id>/', record_views.edit, name='edit'),

    path('goals/', goals_views.show_goals, name='goals'),
    path('goals/add', goals_views.add, name='goals_add'),
    path('goals/edit/<int:goal_id>/', goals_views.edit, name='goals_edit'),
     path('goals/delete/<int:goal_id>/', goals_views.delete, name='goals_delete'),
    #path('goals/', goals_views.show_goals, name='addgoals'),

    #path('addgoals/delete/<int:record_id>/', goals_views.delete, name='delete'),
    #path('addgoals/add/', goals_views.add, name='record_add'),
    #path('addgoals/edit/<int:record_id>/', goals_views.edit, name='edit'),

    path('singup/', sing_views.singup, name='singup'),
    path('user/', sing_views.user, name='user'),
    path('user/edit', sing_views.edit_user, name='user_edit'),

    path('statistics/', statistic_view.show_statistics, name='statistics'),

    path('initial', sing_views.initial, name='initial'),
]