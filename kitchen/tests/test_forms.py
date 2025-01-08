from django.contrib.auth import get_user_model
from django.test import TestCase
from kitchen.forms import *


class ValidateNameFuncTest(TestCase):
    def test_name_with_numbers(self):
        with self.assertRaises(ValidationError) as context:
            validate_name("John123")
        self.assertEqual(
            str(context.exception),
            "['This field should only contain letters']"
        )

    def test_name_with_special_characters(self):
        with self.assertRaises(ValidationError) as context:
            validate_name("John@@@")
        self.assertEqual(
            str(context.exception),
            "['This field should only contain letters']"
        )

    def test_name_with_one_letter(self):
        with self.assertRaises(ValidationError) as context:
            validate_name("J")
        self.assertEqual(
            str(context.exception),
            "['This field should has 2 or more symbols ']"
        )

    def test_name_with_empty_string(self):
        with self.assertRaises(ValidationError) as context:
            validate_name("")
        self.assertEqual(
            str(context.exception),
            "['This field should only contain letters']"
        )


class CookCreationFormTest(TestCase):
    def test_cook_creation_form_valid(self):
        form_data = {
            "username": "testcooker",
            "password1": "testpass123",
            "password2": "testpass123",
            "email": "email@gmail.com",
            "years_of_experience": 12,
            "first_name": "TestFirst",
            "last_name": "TestLast",
        }
        form = CookForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class CookUpdateFormTest(TestCase):
    def test_cook_update_form_valid(self):
        form_data = {"years_of_experience": 12}
        form = CookUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_cook_update_form_invalid(self):
        form_data = {"years_of_experience": "asd"}
        form = CookUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())


class DishFormTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Dish", country="Italy")
        self.cook = get_user_model().objects.create_user(
            username="testcooker",
            email="<EMAIL>",
            password="<PASSWORD>",
            first_name="TestFirst",
            last_name="TestLast",
        )
        self.ingredients1 = Ingredient.objects.create(
            name="Ingredient",
        )
        self.ingredients2 = Ingredient.objects.create(
            name="Ingredient2",
        )

    def test_dish_form_valid(self):
        dish_form = {
            "name": "test",
            "description": "test",
            "cooks": [self.cook.id],
            "price": "12",
            "ingredients": [self.ingredients1.id, self.ingredients2.id],
            "dish_type": self.dish_type.id
        }
        form = DishForm(data=dish_form)
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data["name"], "test")

    def test_invalid_name(self):
        data = {
            "name": "Chicken@123",
            "description": "Delicious grilled chicken",
            "price": "12.50",
            "dish_type": self.dish_type.id,
            "cooks": [self.cook.id],
            "ingredients": [self.ingredients1.id],
        }
        form = DishForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_missing_required_field(self):
        data = {
            "description": "Delicious grilled chicken",
            "price": "12.50",
            "dish_type": self.dish_type.id,
            "cooks": [self.cook.id],
            "ingredients": [self.ingredients1.id],
        }
        form = DishForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_invalid_price(self):
        data = {
            "name": "Grilled Chicken",
            "description": "Delicious grilled chicken",
            "price": "invalid",
            "dish_type": self.dish_type.id,
            "cooks": [self.cook.id],
            "ingredients": [self.ingredients1.id],
        }
        form = DishForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("price", form.errors)

    def test_widgets(self):
        form = DishForm()
        self.assertIsInstance(form.fields["ingredients"].widget, forms.CheckboxSelectMultiple)
        self.assertIsInstance(form.fields["cooks"].widget, forms.CheckboxSelectMultiple)


class DishTypeFormTest(TestCase):
    def test_dish_type_form_valid(self):
        form_data = {
            "name": "test",
            "country": "Italy",
        }
        form = DishTypeForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class IngredientFormTest(TestCase):
    def test_ingredient_form_valid(self):
        form_data = {"name": "test"}
        form = IngredientForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class DishNameSearchFormTest(TestCase):
    def test_dish_name_search_form_valid(self):
        form_data = {"name": "test"}
        form = DishNameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_name_search_form_empty(self):
        form_data = {"name": ""}
        form = DishNameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())


class CookUsernameSearchFormTest(TestCase):
    def test_cook_username_search_form_valid(self):
        form_data = {"username": "test"}
        form = CookUsernameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_cook_username_search_form_empty(self):
        form_data = {"username": ""}
        form = CookUsernameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())


class DishTypeNameSearchFormTest(TestCase):
    def test_dish_type_name_search_form_valid(self):
        form_data = {"name": "test"}
        form = DishTypeNameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_type_name_search_form_empty(self):
        form_data = {"name": ""}
        form = DishTypeNameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())


class IngredientNameSearchFormTest(TestCase):
    def test_ingredient_name_search_form_valid(self):
        form_data = {"name": "test"}
        form = IngredientNameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_ingredient_name_search_form_empty(self):
        form_data = {"name": ""}
        form = IngredientNameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
