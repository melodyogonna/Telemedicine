from django.test import TestCase 

from django.contrib.auth import get_user_model

from usermanager.forms import CustomUserCreationForm, CustomAuthenticationForm

# Create your tests here.
class UserRegisterTest(TestCase):
    """Test wether user registration form works"""

    def setUp(self):
        self.data = dict(first_name='john', last_name='doe',
                email='johndoe@email.com', password1='passworddkkdnknkan443453',
                password2='passworddkkdnknkan443453')


    def test_user_creation_form_works(self):

        create = CustomUserCreationForm(self.data).save()
        self.assertEqual(create.first_name, self.data.get('first_name'))

    
