from uuid import uuid4
import csv

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Count
from django.http import HttpResponse

from audit import models as audit_models
from audit import forms as audit_forms
from .services import form_home_context


@login_required(login_url="login/")
def home(request):
    if request.method == 'POST':
        for _ in range(int(request.POST['amount'])):
            form = audit_forms.StorageForm(request.POST)
            if form.is_valid():
                form.save()
        return redirect('home')

    context = {
        'form': audit_forms.StorageForm(initial={'group': str(uuid4())}),
        'cats': form_home_context()
    }
    return render(request, 'home.html', context)


@login_required(login_url="/")
def categories(request):
    if request.method == 'POST':
        form = audit_forms.CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')

    context = {
        'form': audit_forms.CategoryForm,
        'categories': audit_models.Category.objects.all()
    }
    return render(request, 'categories.html', context)


@login_required(login_url="/")
def items(request):
    if request.method == 'POST':
        form = audit_forms.ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items')

    context = {
        'form': audit_forms.ItemForm,
        'categories': audit_models.Item.objects.all(),
        'items': audit_models.Item.objects.all()
    }
    return render(request, 'items.html', context)


@login_required(login_url="/")
def update_amortizations(request):
    items = audit_models.Storage.objects.filter(item__is_monthly_amortizations=True)
    for item in items:
        item.save()
    return redirect('home')


@login_required(login_url="/")
def shortage(request):
    result = audit_models.Storage.objects.values('item__name', 'item__amount').annotate(count=Count('id'))
    data = []
    for r in result:
        s = r['item__amount'] - r['count']
        r['status'] = 'Недостача' if s > 0 else 'Избыток'
        r['dif'] = s
        data.append(r)
    print(data)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Наименование', 'Количество', 'Количество записей', 'Статус', 'Разница'])

    for item in data:
        writer.writerow([item['item__name'], item['item__amount'], item['count'], item['status'], item['dif']])

    return response