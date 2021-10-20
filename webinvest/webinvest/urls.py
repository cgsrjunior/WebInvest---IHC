from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('invest/', include('invest.urls')),
    path('admin/', admin.site.urls),
]