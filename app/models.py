"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self,email,
                    first_name=None,
                    last_name=None,
                    password=None,
                    address=None,
                    phone_number=None,
                    sex=None,country=None,
                    **extra_fields):
        if not email:
            raise ValueError('L\'adresse e-mail doit être renseignée.')

        email = self.normalize_email(email)
        user = self.model(email=email,first_name=first_name,last_name=last_name,address=address,phone_number=phone_number,sex=sex,country=country, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,email,
        first_name=None,
        last_name=None,
        password=None,
        address=None,
        phone_number=None,
        sex=None,country=None,
        **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email,first_name,last_name,password,address,phone_number,sex,country,**extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
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
    USERNAME_FIELD = 'email'
    
    first_name = models.CharField(_("first name"),blank=False,max_length=30)
    last_name = models.CharField(_("last name"),blank=False,max_length=30)
    email = models.EmailField(_("email"),unique=True,blank=True)
    address = models.CharField(_("address"),blank=True,max_length=255)
    phone_number = models.CharField(_("phone_number"),unique=True,max_length=30,blank=True)
    sex = models.CharField(_("sex"),max_length=1, choices=GENDER_CHOICES, default='M')
    country = models.CharField(_("country"),max_length=50,choices=COUNTRY_CHOICES,default='GA')
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(_("joined_date "), auto_now_add=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
