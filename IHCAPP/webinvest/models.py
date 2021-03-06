from django.db import models
from django.forms import ModelForm, DateInput
import datetime
from crispy_forms.helper import FormHelper

#Records class

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 



class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class TypeForm(ModelForm):
    class Meta:
        model = Type
        fields = ['name']
        
    def __init__(self, *args, **kwargs):
        super(TypeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 



class Record(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    value = models.FloatField(default=0.0)
    pub_date = models.DateTimeField(default=datetime.datetime.now , blank=True)

    def __str__(self):
        return self.title

class DateInput(DateInput):
    input_type = 'date'

class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
        widgets = {
            'pub_date': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(RecordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 


