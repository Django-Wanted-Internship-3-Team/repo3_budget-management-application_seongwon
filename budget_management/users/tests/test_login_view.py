import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from budget_management.users.models import User


class SignupViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="testusername1", password="testpassword")

    def test_post_login_success(self):
        response = self.client.post(
            path=reverse("login"),
            data=json.dumps(
                {
                    "username": "testusername1",
                    "password": "testpassword",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user.is_active, True)

    def test_post_login_fail_user_not_found(self):
        response = self.client.post(
            path=reverse("login"),
            data=json.dumps(
                {
                    "username": "testusername3",
                    "password": "testpassword",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_login_fail_invalid_password(self):
        response = self.client.post(
            path=reverse("login"),
            data=json.dumps(
                {
                    "username": "testusername1",
                    "password": "testpassword2",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
