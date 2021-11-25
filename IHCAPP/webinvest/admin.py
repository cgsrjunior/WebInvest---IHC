from django.contrib import admin
from .models import Category
from .models import Record
from .models import Type
from .models import Priority
from .models import Goal

admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Record)
admin.site.register(Priority)
admin.site.register(Goal)