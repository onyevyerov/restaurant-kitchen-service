from django.test import TestCase

from kitchen.models import DishType, Cook, Dish, Ingredient


class ModelTests(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Test", country="TestCountry")
        self.dish = Dish.objects.create(
            name="Test",
            description="Test",
            price=10,
            dish_type=self.dish_type,
        )
        self.cook = Cook.objects.create(
            username="TestUser",
            password="<PASSWORD>",
            first_name="TestFirstName",
            last_name="TestLastName",
            years_of_experience=2,
        )
        self.ingredient = Ingredient.objects.create(
            name="Ingredient",
        )
        self.dish.cooks.add(self.cook)
        self.dish.ingredients.add(self.ingredient)

    def test_dish_type_str(self):
        self.assertEqual(str(self.dish_type), "Test")

    def test_cook_str(self):
        self.assertEqual(str(self.cook), "TestUser (TestFirstName TestLastName)")

    def test_dish_str(self):
        self.assertEqual(str(self.dish), "Test")

    def test_ingredient_str(self):
        self.assertEqual(str(self.ingredient), "Ingredient")
