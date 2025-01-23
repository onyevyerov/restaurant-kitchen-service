from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from kitchen.models import Dish, DishType

DISH_LIST_URL = reverse("kitchen:dish-list")


class PublicDishTest(TestCase):
    def test_login_required(self):
        response = self.client.get(DISH_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateDishTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="<PASSWORD>",
        )
        self.client.force_login(self.user)

        self.dish_type1 = DishType.objects.create(name="pizza", country="Italy")
        self.dish_type2 = DishType.objects.create(name="stake", country="USA")
        self.dish1 = Dish.objects.create(
            name="Margherita",
            price=10,
            dish_type=self.dish_type1,
        )
        self.dish2 = Dish.objects.create(
            name="rebai",
            price=15,
            dish_type=self.dish_type2,
        )

    def test_retrieve_dish_list(self):
        response = self.client.get(DISH_LIST_URL)
        self.assertEqual(response.status_code, 200)

        dishes = Dish.objects.all()

        self.assertEqual(list(response.context["dish_list"]), list(dishes))
        self.assertTemplateUsed(response, "kitchen/dish_list.html")

    def test_get_context_data(self):
        response = self.client.get(DISH_LIST_URL, {"name": "rebai"})
        search_form = response.context["search_form"]

        self.assertEqual(search_form.initial["name"], "rebai")

    def test_get_queryset_with_search(self):
        response = self.client.get(DISH_LIST_URL, {"name": "rebai"})
        dish = Dish.objects.filter(name__icontains="rebai")

        self.assertEqual(list(response.context["dish_list"]), list(dish))
