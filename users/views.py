from django.shortcuts import render
from audit import models as audit_models


def home(request):
    storage = audit_models.Storage.objects.all()
    context = {'storage': storage}
    return render(request, 'home.html', context)
