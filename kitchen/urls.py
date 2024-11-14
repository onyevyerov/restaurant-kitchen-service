from django.urls import path

from kitchen.views import index, DishListView, CookListView

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
]

app_name = "kitchen"
