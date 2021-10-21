from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from webinvest.models import Record, RecordForm

from django.forms import modelformset_factory
from django.shortcuts import render

def show_statistics(request):
    template ='webinvest/estatisticas/index.html'

    context = {}

    #goals = Goals.objects.all()
    #context['goals'] = goals

    return render(request, template, context)



