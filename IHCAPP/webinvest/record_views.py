from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from webinvest.models import Record, RecordForm

from django.forms import modelformset_factory
from django.shortcuts import render


def show_records(request, column_name=None, order=None, ):
    template = 'webinvest/record.html'

    context = {}

    try:
        query = request.POST.get("query", "")
    except:
        query = ""
        

    if column_name == None:
        column = 'title'
    else:
        column = column_name
    
    if order == 'desc':
        prox_order = 'asc'
        records = Record.objects.all().filter(title__contains=query).order_by(column).reverse()
    else:
        prox_order = 'desc'
        records = Record.objects.all().filter(title__contains=query).order_by(column)
    
    context['records'] = records
    context['prox_order'] = prox_order
    context['query'] = query

    return render(request, template, context)


def delete(request, record_id):
    Record.objects.filter(id=record_id).delete()

    return show_records(request)


def add(request):
    template = 'webinvest/record_add.html'
    context = {}

    if request.method == "POST":
        record_form = RecordForm(request.POST, request.FILES)

        if record_form.is_valid():
            record_form.save()
            return show_records(request)
    else:
        record_form = RecordForm()

    context['record_form'] = record_form

    return render(request, template, context)


def edit(request, record_id=None):
    template = 'webinvest/record_add.html'
    context = {}

    record = Record.objects.get(pk=record_id)

    if request.method == 'POST':
        record_form = RecordForm(request.POST, instance=record)
        if record_form.is_valid():
            record_form.save()
            return show_records(request)
    else:
        record_form = RecordForm(instance=record)

    context['record_form'] = record_form

    return render(request, template, context)

    '''title = request.POST['title']
    category = request.POST['category']
    value = request.POST['value']
    pub_date = request.POST['pub_date']

    return HttpResponse("Você está adicionando o registro")
    '''


'''
def detail(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    records = Record.objects.all()

    context = {}
    template = 'webinvest/detail.html'

    context['record'] = record
    context['records'] = records

    if request.method == 'POST':
        formset = RecordForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = RecordForm()

    context['formset'] = formset
'''
