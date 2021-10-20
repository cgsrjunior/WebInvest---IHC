from django.contrib import admin
from .models import Category
from .models import Record
from .models import Type

admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Record)