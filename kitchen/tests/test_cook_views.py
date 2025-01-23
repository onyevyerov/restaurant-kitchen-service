from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Cook

COOK_LIST_URL = reverse("kitchen:cook-list")


class PublicCookViewTest(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="testuser",
            password="<PASSWORD>",
        )
        self.cook1 = get_user_model().objects.create_user(
            username="testuser1",
            password="<PASSWORD>",
        )

    def test_login_required(self):
        response = self.client.get(COOK_LIST_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_detailed_login_required(self):
        response = self.client.get(reverse("kitchen:cook-detail", args=[self.cook.id]))
        self.assertNotEqual(response.status_code, 200)


class PrivateCookViewTest(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="testuser",
            password="<PASSWORD>",
        )
        self.client.force_login(self.cook)
        self.cook1 = get_user_model().objects.create_user(
            username="testuser1",
            password="<PASSWORD>",
        )
        self.cook2 = get_user_model().objects.create_user(
            username="testuser2",
            password="<PASSWORD>",
        )

    def test_retrieve_cook_list(self):
        response = self.client.get(COOK_LIST_URL)
        cooks = Cook.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["cook_list"]), list(cooks))
        self.assertTemplateUsed(response, "kitchen/cook_list.html")

    def test_get_context_data(self):
        response = self.client.get(COOK_LIST_URL, {"username": "testuser1"})
        search_form = response.context["search_form"]
        self.assertEqual(search_form.initial["username"], "testuser1")

    def test_get_queryset_with_search(self):
        response = self.client.get(COOK_LIST_URL, {"username": "testuser1"})
        cooks = Cook.objects.filter(username__icontains="testuser1")
        self.assertEqual(list(response.context["cook_list"]), list(cooks))
