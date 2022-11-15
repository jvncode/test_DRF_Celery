from django.db import models

class UserRegister(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nombre')
    surnames = models.CharField(max_length=100, null=False, blank=False, verbose_name='Apellidos')
    email = models.EmailField(max_length=200, null=False, blank=False, verbose_name='Correo electrónico')
    phone = models.IntegerField(null=False, blank=False, verbose_name='Móvil')
    hobbies = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Aficiones')

    def __str__(self):
        return f"{self.name} {self.surnames}"
