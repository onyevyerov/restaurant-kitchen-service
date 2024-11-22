from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import DishForm, CookForm, DishTypeForm, CookUpdateForm
from kitchen.models import Dish, Cook, DishType, Ingredient


def index(request: HttpRequest) -> HttpResponse:
    num_of_dishes = Dish.objects.count()
    num_of_cooks = Cook.objects.count()
    num_of_dish_types = DishType.objects.count()
    num_of_ingredients = Ingredient.objects.count()

    context = {
        "num_of_dishes": num_of_dishes,
        "num_of_cooks": num_of_cooks,
        "num_of_dish_types": num_of_dish_types,
        "num_of_ingredients": num_of_ingredients,
    }
    return render(request, "kitchen/index.html", context=context)


class DishListView(generic.ListView, LoginRequiredMixin):
    model = Dish


class DishCreateView(generic.CreateView, LoginRequiredMixin):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishDetailView(generic.DetailView, LoginRequiredMixin):
    model = Dish


class DishUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(generic.DeleteView, LoginRequiredMixin):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")
    template_name = "kitchen/dish_confirm_delete.html"


class CookListView(generic.ListView, LoginRequiredMixin):
    model = Cook


class CookCreateView(generic.CreateView, LoginRequiredMixin):
    model = Cook
    form_class = CookForm
    success_url = reverse_lazy("kitchen:cook-list")


class CookDetailView(generic.DetailView, LoginRequiredMixin):
    model = Cook


class CookUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")
    form_class = CookUpdateForm


class CookDeleteView(generic.DeleteView, LoginRequiredMixin):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")
    template_name = "kitchen/cook_confirm_delete.html"


class DishTypeListView(generic.ListView, LoginRequiredMixin):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_list.html"


class DishTypeCreateView(generic.CreateView, LoginRequiredMixin):
    model = DishType
    form_class = DishTypeForm
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_form.html"
    context_object_name = "dish_type"


class DishTypeDeleteView(generic.DeleteView, LoginRequiredMixin):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_confirm_delete.html"
    context_object_name = "dish_type"


class DishTypeUpdateView(generic.UpdateView, LoginRequiredMixin):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
    form_class = DishTypeForm
    template_name = "kitchen/dish_type_form.html"
    context_object_name = "dish_type"


class DishTypeDetailView(generic.DetailView, LoginRequiredMixin):
    model = DishType
    context_object_name = "dish_type"
    template_name = "kitchen/dish_type_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["dishes"] = Dish.objects.filter(dish_type=self.object)
        return context
