from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status

from usermanager.forms import CustomUserCreationForm, CustomAuthenticationForm

API_ROUTE = "/api/v1/"

# Create your tests here.
class UserRegisterTest(APITestCase):
    """Test wether user registration form works"""

    def setUp(self):
        self.data = dict(
            first_name="john",
            last_name="doe",
            email="johndoe@email.com",
            password1="passworddkkdnknkan443453",
            password2="passworddkkdnknkan443453",
        )

    def test_user_creation_form_works(self):

        create = CustomUserCreationForm(self.data).save()
        self.assertEqual(create.first_name, self.data.get("first_name"))

    def test_user_register_route(self):
        response = self.client.post(API_ROUTE + "register/", self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
