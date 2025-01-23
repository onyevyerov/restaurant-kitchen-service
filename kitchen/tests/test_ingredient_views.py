from django.contrib.auth import get_user_model
from django.test import TestCase
from kitchen.models import Ingredient
from django.urls import reverse

INGREDIENT_LIST_URL = reverse("kitchen:ingredient-list")


class PublicIngredientViewTest(TestCase):
    def test_login_required(self):
        response = self.client.get(INGREDIENT_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateIngredientViewTest(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="testuser",
            password="<PASSWORD>",
        )
        self.client.force_login(self.cook)

        self.ingredient1 = Ingredient.objects.create(name="Onion")
        self.ingredient2 = Ingredient.objects.create(name="Garlic")

    def test_retrieve_ingredient_list(self):
        response = self.client.get(INGREDIENT_LIST_URL)
        ingredients = Ingredient.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["ingredient_list"]), list(ingredients))
        self.assertTemplateUsed(response, "kitchen/ingredient_list.html")

    def test_get_context_data(self):
        response = self.client.get(INGREDIENT_LIST_URL, {"name": "Onion"})
        search_form = response.context["search_form"]

        self.assertEqual(search_form.initial["name"], "Onion")

    def test_get_queryset_with_search(self):
        response = self.client.get(INGREDIENT_LIST_URL, {"name": "Onion"})
        ingredients = Ingredient.objects.filter(name__icontains="Onion")

        self.assertQuerysetEqual(
            list(response.context["ingredient_list"]), list(ingredients)
        )
