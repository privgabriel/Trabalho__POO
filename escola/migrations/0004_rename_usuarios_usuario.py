# Generated by Django 4.2.7 on 2023-12-03 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_usuarios'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuarios',
            new_name='Usuario',
        ),
    ]