from django import forms
from .models import Item, Category, Storage


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class StorageForm(forms.ModelForm):
    amount = forms.IntegerField()

    class Meta:
        model = Storage
        exclude = ('expiration_date', 'current_price')
