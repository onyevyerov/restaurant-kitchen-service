from django.urls import path

from kitchen.views import (
    index,
    DishListView,
    CookListView,
    DishTypeListView,
    DishCreateView,
    CookCreateView,
    DishTypeCreateView,
    DishDetailView,
    CookDetailView,
    DishDeleteView,
    CookDeleteView,
    DishTypeDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/detail/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/detail/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish-types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
]

app_name = "kitchen"
