"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'adresse e-mail doit être renseignée.')

        email = self.normalize_email(email)
        user = self.model(username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    GENDER_CHOICES = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    )
    COUNTRY_CHOICES = (
        ('GA', 'Gabon'),
        ('TR', 'Türkiye'),
        ('FR', 'France'),
    )
    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'username'
    
    first_name = models.CharField(_("first name"),blank=False,max_length=30)
    last_name = models.CharField(_("last name"),blank=False,max_length=30)
    username = models.EmailField(_("username"),unique=True,blank=True)
    nick_name = models.CharField(_("nick name "),blank=True,max_length=30)
    address = models.CharField(_("address"),blank=True,max_length=255)
    phone_number = models.CharField(_("phone number"),unique=True,max_length=30,blank=True)
    sex = models.CharField(_("sex"),max_length=1, choices=GENDER_CHOICES, default='M')
    country = models.CharField(_("country"),max_length=50,choices=COUNTRY_CHOICES,default='GA')
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_("joined date "), auto_now_add=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
