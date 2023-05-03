from audit import models as audit_models


def add_items_to_storage(item, amount):
    pass


def form_home_context():
    cats = {}

    categories = audit_models.Category.objects.all()
    for cat in categories:
        objs = audit_models.Storage.objects.filter(item__category=cat)
        cats[str(cat)] = objs

    return cats
