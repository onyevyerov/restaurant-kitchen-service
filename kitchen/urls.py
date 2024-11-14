from django.urls import path

from kitchen.views import (
    index,
    DishListView,
    CookListView,
    DishTypeListView,
    DishCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
]

app_name = "kitchen"
