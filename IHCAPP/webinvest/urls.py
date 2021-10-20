from django.urls import path

from webinvest import goals_views
from webinvest import sing_views

from . import record_views

app_name = 'webinvest'
urlpatterns = [
    path('', record_views.show_records, name='index'),
    path('record/', record_views.show_records, name='record'),
    path('record/<int:record_id>/delete/', record_views.delete, name='delete'),
    path('record/add/', record_views.add, name='add'),
    path('record/<int:record_id>/edit/', record_views.edit, name='edit'),

    path('goals/', goals_views.show_goals, name='goals'),

     path('singup/', sing_views.singup, name='singup'),
]