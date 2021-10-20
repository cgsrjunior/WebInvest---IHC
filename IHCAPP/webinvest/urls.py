from django.urls import path

from . import record_views

app_name = 'webinvest'
urlpatterns = [
    path('', record_views.show_records, name='index'),
    path('record/', record_views.show_records, name='record'),
    path('record/<int:record_id>/delete/', record_views.delete, name='record_delete'),
    path('record/add/', record_views.add, name='record_add'),
    path('record/<int:record_id>/edit/', record_views.edit, name='record_edit'),

]