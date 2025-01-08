from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin123",
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="cook",
            password="cook123",
            first_name="Max",
            last_name="Jones",
            years_of_experience=2,
        )

    def test_cook_years_of_experience_field_listed(self):
        """
        Test that cook's years of experience field is in list_display on admin page
        """
        url = reverse("admin:kitchen_cook_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.cook.years_of_experience)

    def test_cook_detailed_years_of_experience_listed(self):
        """
        Test that cook's years of experience is in fieldsets on admin page
        """
        url = reverse("admin:kitchen_cook_change", args=[self.cook.pk])
        response = self.client.get(url)
        self.assertContains(response, self.cook.years_of_experience)

    def test_add_fieldsets_in_cook_admin(self):
        """
        Test that First name, Last name, Years of experience fields
        are in the add_fieldsets on the add cook page
        """
        url = reverse("admin:kitchen_cook_add")
        response = self.client.get(url)
        self.assertContains(response, "first_name")
        self.assertContains(response, "last_name")
        self.assertContains(response, "years_of_experience")
