from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('categories/', categories, name='categories'),
    path('items/', items, name='items'),
    path('update/', update_amortizations, name='update'),
    path('shortage/', shortage, name='shortage'),
]