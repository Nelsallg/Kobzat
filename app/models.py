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
        user = self.model(email=email, **extra_fields)
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

    first_name = models.CharField(blank=False,max_length=30)
    last_name = models.CharField(blank=False,max_length=30)
    email = models.EmailField(unique=True)
    nickname = models.CharField(blank=True,max_length=30)
    address = models.CharField(blank=True,max_length=100)
    phone_number = models.CharField(max_length=15)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    country = models.CharField(blank=True,max_length=50)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateField(_("Dernière connexion"), auto_now=False, auto_now_add=False)
    date_joined = models.DateTimeField(_("Date d'inscription"), auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'nickname', 'address', 'phone_number', 'sex', 'country']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
