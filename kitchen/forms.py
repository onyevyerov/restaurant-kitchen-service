from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from kitchen.models import Dish, Cook


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = '__all__'


class CookForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = '__all__'
