from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from webinvest.models import Record, RecordForm

from django.forms import modelformset_factory
from django.shortcuts import render

def singup(request):
    template ='webinvest/singup.html'

    context = {}

    #goals = Goals.objects.all()
    #context['goals'] = goals

    return render(request, template, context)

def user(request):
    template ='webinvest/user.html'

    context = {}

    #goals = Goals.objects.all()
    #context['goals'] = goals

    return render(request, template, context)

def edit_user(request):
    template ='webinvest/edituser.html'

    context = {}

    #goals = Goals.objects.all()
    #context['goals'] = goals

    return render(request, template, context)

def initial(request):
    template ='webinvest/first.html'

    context = {}

    #goals = Goals.objects.all()
    #context['goals'] = goals

    return render(request, template, context)


