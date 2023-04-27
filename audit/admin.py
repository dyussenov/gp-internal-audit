from django.contrib import admin
from .models import *
from .forms import ItemForm


class ItemAdmin(admin.ModelAdmin):
    add_form = ItemForm
    form = ItemForm
    list_display = ['id', 'name', 'category', 'amortization', 'operation_life', 'receive_date', 'expiration_date']


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
