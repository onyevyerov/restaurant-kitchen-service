from django.urls import path

from kitchen.views import index, DishListView

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
]

app_name = "kitchen"
