from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

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
