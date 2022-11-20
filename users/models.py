from django.db import models
from django.contrib.auth.models import User, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import UserManager


class Profile(AbstractBaseUser, PermissionsMixin):
    User.username = None

    name = models.CharField(
                            max_length=50,
                            null=False,
                            blank=False,
                            verbose_name='Nombre')
    surnames = models.CharField(
                            max_length=100,
                            null=False,
                            blank=False,
                            verbose_name='Apellidos')
    email = models.EmailField(
                            max_length=200,
                            null=False,
                            blank=False,
                            verbose_name='Correo electrónico',
                            unique=True)
    phone = models.IntegerField(
                            null=True,
                            blank=True,
                            verbose_name='Móvil')
    hobbies = models.TextField(
                            max_length=2000,
                            null=True,
                            blank=True,
                            verbose_name='Aficiones')
    verified_email = models.BooleanField(
                            verbose_name='Correo_verificado',
                            default=0,
                            blank=True)
    verified_phone = models.BooleanField(
                            verbose_name='Móvil verificado',
                            default=0,
                            blank=True)
    is_staff = models.BooleanField(
                            verbose_name='Staff status',
                            default=False)
    is_active = models.BooleanField(
                            verbose_name='Active',
                            default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.name} {self.surnames}"
