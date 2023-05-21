from audit import models as audit_models


def add_items_to_storage(item, amount):
    pass


def form_home_context():
    cats = {}

    categories = audit_models.Category.objects.all()
    for cat in categories:
        objs = audit_models.Storage.objects.filter(item__category=cat)
        cat_name = str(cat)
        cats[cat_name] = {}
        for o in objs:
            if o.group not in cats[cat_name]:
                cats[cat_name][o.group] = []
                cats[cat_name][o.group].append(o)
            else:
                cats[cat_name][o.group].append(o)




    print(cats)
    return cats
