"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(UserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError('L\'adresse e-mail doit être renseignée.')

        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email,password,**extra_fields)



class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    )
    COUNTRY_CHOICES = (
        ('GA', 'Gabon'),
        ('TR', 'Türkiye'),
        ('FR', 'France'),
    )
    
    email = models.EmailField(_("email address"), unique=True,max_length=255)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    address = models.CharField(_("address"), blank=True, max_length=255, null=True)
    phone_number = models.CharField(_("phone_number"), unique=True, max_length=30, blank=True, null=True)
    sex = models.CharField(_("sex"), max_length=1, choices=GENDER_CHOICES, default='M')
    country = models.CharField(_("country"), max_length=50, choices=COUNTRY_CHOICES, default='GA')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(_("joined date"), auto_now_add=True)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'auth_user'
