# Generated by Django 5.0.6 on 2024-07-09 15:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_extension', '0004_rename_employee_extenson'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Extenson',
            new_name='Extension',
        ),
    ]
