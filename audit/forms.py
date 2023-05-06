from django import forms
from .models import Item, Category, Storage


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        labels = {
            'name': 'Наименование',
            'category': 'Категория',
            'price': 'Цена',
            'amortization': 'Процент амортизации',
            'is_monthly_amortizations': 'Ежемесячная амортизация',
            'image': 'Изображение',
            'operation_life': 'Срок эксплуатации'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Выберите категорию"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': 'Наименование',
            'description': 'Описание'
        }


class StorageForm(forms.ModelForm):
    amount = forms.IntegerField(label="Количество")

    class Meta:
        model = Storage
        exclude = ('expiration_date', 'current_price')
        labels = {
            "item": "Предмет",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].empty_label = "Выберите тип"
