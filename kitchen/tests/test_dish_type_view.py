from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from kitchen.models import DishType

DISH_TYPE_LIST_USL = reverse("kitchen:dish-type-list")


class PublicDishTypeViewTest(TestCase):
    def test_login_required(self):
        response = self.client.get(DISH_TYPE_LIST_USL)
        self.assertNotEqual(response.status_code, 200)


class PrivateDishTypeViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="TestUser",
            password="<PASSWORD>",
            first_name="TestFirst",
            last_name="TestLast",
        )
        self.client.force_login(self.user)

        self.dish_type1 = DishType.objects.create(name="DishType1", country="Italy")
        self.dish_type2 = DishType.objects.create(name="DishType2", country="China")

    def test_dish_type_list_retrieve(self):
        response = self.client.get(DISH_TYPE_LIST_USL)
        self.assertEqual(response.status_code, 200)

        dish_types = DishType.objects.all()
        self.assertEqual(list(response.context["dish_type_list"]), list(dish_types))

        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")

    def test_get_context_data(self):
        response = self.client.get(DISH_TYPE_LIST_USL, {"name": "DishType1"})
        search_form = response.context["search_form"]
        self.assertEqual(search_form.initial["name"], "DishType1")

    def test_get_queryset_with_search(self):
        response = self.client.get(DISH_TYPE_LIST_USL, {"name": "DishType1"})
        dish_type = DishType.objects.filter(name__icontains="DishType1")
        self.assertEqual(list(response.context["dish_type_list"]), list(dish_type))
