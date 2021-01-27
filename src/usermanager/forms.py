# Standard library
import logging

# Third-party dependencies
from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from django.utils.translation import gettext, gettext_lazy as _


# User defined modules
from usermanager.models import CustomUser

UserModel = get_user_model()


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']

    def save(self):
        user = super().save()
        return user

class CustomUserChangeForm(UserChangeForm):
    """Extend default form change"""
    class Meta:
        """Meta data for custom field"""
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class CustomAuthenticationForm(forms.Form):
    username = None
    email = forms.EmailField()
    password = forms.CharField(strip=False, widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None

        self.username_field = UserModel._meta.get_field(
            UserModel.USERNAME_FIELD)

        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(
                self.request, email=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()

        return self.cleaned_data

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return forms.ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'username': self.username_field.verbose_name},
        )
