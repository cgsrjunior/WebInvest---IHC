from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('webinvest/', include('webinvest.urls')),
    path('admin/', admin.site.urls),
]