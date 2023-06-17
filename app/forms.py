"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,widget=forms.TextInput(
        {
            'class': 'form-control',
            'placeholder': 'Email ou pseudo'
        }
    ))
    password = forms.CharField(label=_("Password"),widget=forms.PasswordInput(
        {
            'class': 'form-control',
            'placeholder':'Mot de passe'
        }
    ))