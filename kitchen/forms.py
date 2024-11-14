from django.forms import ModelForm

from kitchen.models import Dish


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = '__all__'
