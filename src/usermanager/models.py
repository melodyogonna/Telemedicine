from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    '''Custom user model, uses email for login'''

    email = models.EmailField('email address', unique=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    user_choices = (('d', 'doctor'), ('u', 'user'))
    user_type = models.CharField(max_length=1, choices=user_choices, default='u')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
