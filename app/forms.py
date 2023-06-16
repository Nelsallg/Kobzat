"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    nickname_or_email = forms.CharField(max_length=254,widget=forms.TextInput(
        {
            'class': 'form-control',
            'placeholder': 'Email ou pseudo'
        }
    ))
    password = forms.CharField(label=_("Mot de passe"),widget=forms.PasswordInput(
        {
            'class': 'form-control',
            'placeholder':'Mot de passe'
        }
    ))