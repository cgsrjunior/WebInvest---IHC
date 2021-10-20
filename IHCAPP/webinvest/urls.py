from django.urls import path

from . import record_views

app_name = 'webinvest'
urlpatterns = [
    path('', record_views.show_records, name='record'),
    path('record/', record_views.show_records, name='record'),
    path('record/<int:record_id>/delete/', record_views.delete, name='delete'),
    path('record/add/', record_views.add, name='add'),
    path('record/<int:record_id>/edit/', record_views.edit, name='edit'),

]