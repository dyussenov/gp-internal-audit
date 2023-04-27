from django.shortcuts import render
from audit import models as audit_models


def home(request):
    cats = {}

    categories = audit_models.Category.objects.all()
    for cat in categories:
        objs = audit_models.Storage.objects.filter(item__category=cat)
        print(objs)
        cats[str(cat)] = objs

    context = {
        'cats': cats
    }
    print(context)
    return render(request, 'home.html', context)
