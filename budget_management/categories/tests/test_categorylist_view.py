import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from budget_management.categories.models import Category
from budget_management.users.models import User


class CategoryListViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testusername",
            password="testpassword",
        )
        Category.objects.create(name="testcategory1")
        Category.objects.create(name="testcategory2")
        Category.objects.create(name="testcategory3")

    def setUp(self):
        response = self.client.post(
            path=reverse("login"),
            data=json.dumps(
                {
                    "username": "testusername",
                    "password": "testpassword",
                }
            ),
            content_type="application/json",
        )
        self.access_token = response.data["token"]["access"]

    def test_get_categorylist_success(self):
        response = self.client.get(path=reverse("category_list"), HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_categorylist_fail_unauthorized_user(self):
        response = self.client.get(
            path=reverse("category_list"),
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
