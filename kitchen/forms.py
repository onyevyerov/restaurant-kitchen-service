from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from kitchen.models import Dish, Cook, DishType, Ingredient


def validate_name(value):
    if not value.isalpha():
        raise ValidationError("This field should only contain letters")
    if len(value) < 2:
        raise ValidationError("This field should has 2 or more symbols ")


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"
        widgets = {
            "ingredients": forms.CheckboxSelectMultiple(),
            "cooks": forms.CheckboxSelectMultiple(),
        }


class CookForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )

    first_name = forms.CharField(
        max_length=50,
        validators=[validate_name],
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    last_name = forms.CharField(
        max_length=50,
        validators=[validate_name],
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["years_of_experience"]


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"


class DishNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=55,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by dish name"}),
    )


class CookUsernameSearchForm(forms.Form):
    username = forms.CharField(
        max_length=55,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
    )


class DishTypeNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=55,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by dish type name"}),
    )


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"


class IngredientNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=55,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by ingredient name"}),
    )
