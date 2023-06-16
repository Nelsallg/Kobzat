from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    phone_number = forms.CharField(required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone_number = cleaned_data.get('phone_number')

        if not email and not phone_number:
            raise ValidationError("Veuillez fournir une adresse e-mail ou un numéro de téléphone.")

        return cleaned_data
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'nickname', 'address', 'sex', 'country']
        labels = {
            'first_name': 'Prénom',
            'last_name': 'Nom de famille',
            'email': 'Adresse e-mail',
            'nickname': 'Pseudo',
            'address': 'Adresse',
            'phone_number': 'Numéro de téléphone',
            'sex': 'Sexe',
            'country': 'Pays',
        }
        error_messages = {
            'first_name': {
                'unique': "Le prénom est obligatoire.",
            },
            'last_name': {
                'unique': "Le nom de famille est obligatoire.",
            },
            'email': {
                'unique': "Cette adresse e-mail est déjà utilisée.",
            },
            'phone_number': {
                'unique': "Ce numéro de téléphone est déjà utilisé.",
            },
        }

    def save(self, commit=True):
        user = super(UserRegistrationForm,self).save(commit=False)
        if commit:
            user.save()
        return user
