# Generated by Django 3.2.16 on 2022-11-15 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('surnames', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('email', models.URLField(verbose_name='Correo electrónico')),
                ('phone', models.IntegerField(verbose_name='Móvil')),
                ('hobbies', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Aficiones')),
            ],
        ),
    ]
