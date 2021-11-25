from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from webinvest.models import Goal, GoalForm

from django.forms import modelformset_factory
from django.shortcuts import render

from django.db.models import F, Func

def show_goals(request):
    template ='webinvest/goals.html'

    context = {}

    #goals = Goal.objects.all()
    goals = Goal.objects.annotate(
        percent=( 
                Func(((F('value_acc') * 100) / F('goal_defined')), function='ROUND')
                     ))
                     
    #F('num_employees') - F('num_chairs'))
    context['goals'] = goals

    return render(request, template, context)


def delete(request, goal_id):
    Goal.objects.filter(id=goal_id).delete()

    return show_goals(request)


def add(request):
    template = 'webinvest/goals_add.html'
    context = {}

    if request.method == "POST":
        goal_form = GoalForm(request.POST, request.FILES)

        if goal_form.is_valid():
            goal_form.save()
            return show_goals(request)
    else:
        goal_form = GoalForm()

    context['goal_form'] = goal_form

    return render(request, template, context)


def edit(request, goal_id=None):
    template = 'webinvest/goals_add.html'
    context = {}

    goal = Goal.objects.get(pk=goal_id)

    if request.method == 'POST':
        goal_form = GoalForm(request.POST, instance=goal)
        if goal_form.is_valid():
            goal_form.save()
            return show_goals(request)
    else:
        goal_form = GoalForm(instance=goal)

    context['goal_form'] = goal_form

    return render(request, template, context)


