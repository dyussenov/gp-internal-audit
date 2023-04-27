from django.contrib import admin
from .models import *
from .forms import ItemForm, StorageForm


class ItemAdmin(admin.ModelAdmin):
    add_form = ItemForm
    form = ItemForm
    list_display = ['id', 'name', 'category', 'price', 'amortization', 'operation_life']


class StorageAdmin(admin.ModelAdmin):
    add_form = StorageForm
    form = StorageForm
    list_display = ['id', 'item', 'receive_date', 'expiration_date', 'current_price']


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Storage, StorageAdmin)
