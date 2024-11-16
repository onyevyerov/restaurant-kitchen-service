from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from kitchen.models import Dish, Cook, DishType


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = '__all__'


class CookForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True


class DishTypeForm(ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"
