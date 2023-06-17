from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import User
from django.core.exceptions import ValidationError

WIDGET_ATTRS = {
    'first_name': {
        'placeholder': 'Votre prénom',
    },
    'last_name': {
        'placeholder': 'Votre nom de famille',
    },
    'username': {
        'placeholder': 'Votre adresse e-mail',
    },
    'phone_number': {
        'placeholder': 'Votre numéro de téléphone',
    },
    'nick_name': {
        'placeholder': 'Votre surnom',
    },
    'address': {
        'placeholder': 'Votre addresse',
    }
    
}

class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setHtmlAttributes()
        self.setErrorMessages()
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        
    email = forms.EmailField(required=False)
    phone_number = forms.CharField(required=False)
    
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('username')
        phone_number = cleaned_data.get('phone_number')

        if not email and not phone_number:
            raise ValidationError("Veuillez fournir une adresse e-mail ou un numéro de téléphone.")

        return cleaned_data
    
    def setHtmlAttributes(self):
        for field_name in self.fields:
            field = self.fields[field_name]
            widget = field.widget
            attrs = WIDGET_ATTRS.get(field_name, "")
            widget.attrs.update(attrs)
            
    def setErrorMessages(self):
        self.fields['first_name'].error_messages = {
            'blank': "Le prénom est obligatoire."
        }
        self.fields['last_name'].error_messages = {
            'blank': "Le nom de famille est obligatoire."
        }
        self.fields['username'].error_messages = {
            'unique': "Un utilisateur avec cette adresse e-mail existe déjà."
        }
        self.fields['phone_number'].error_messages = {
            'unique': "Un utilisateur avec ce numéro de téléphone existe déjà."
        }
       
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'nick_name', 'address', 'sex', 'country','phone_number']
        
        labels = {
            'first_name': 'Prénom',
            'last_name': 'Nom de famille',
            'username': 'Adresse e-mail',
            'nick_name': 'Surnom',
            'address': 'Adresse',
            'phone_number': 'Numéro de téléphone',
            'sex': 'Sexe',
            'country': 'Pays',
        }

    def save(self, commit=True):
        user = super(UserRegistrationForm,self).save(commit=False)
        if commit:
            user.save()
        return user

class UserLoginForm:
    pass