from django import forms
from django.contrib.auth.forms import UserCreationForm
from kitchen.models import Dish, Cook, DishType, Ingredient


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = '__all__'
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
            "years_of_experience",
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
