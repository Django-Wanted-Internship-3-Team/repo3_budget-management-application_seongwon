import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from budget_management.users.models import User


class SignupViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testusername1",
            password="testpassword",
        )

    def test_post_signup_success(self):
        response = self.client.post(
            path=reverse("signup"),
            data=json.dumps(
                {
                    "username": "testusername2",
                    "password": "testpassword",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_signup_fail_already_existing_username(self):
        response = self.client.post(
            path=reverse("signup"),
            data=json.dumps(
                {
                    "username": "testusername1",
                    "password": "1234",
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
