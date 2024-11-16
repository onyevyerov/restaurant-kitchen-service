from django.urls import path

from kitchen.views import (
    index,
    DishListView,
    CookListView,
    DishTypeListView,
    DishCreateView,
    CookCreateView,
    DishTypeCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),

]

app_name = "kitchen"
