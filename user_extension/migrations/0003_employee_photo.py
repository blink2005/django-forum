# Generated by Django 5.0.6 on 2024-07-09 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_extension', '0002_remove_employee_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.TextField(null=True),
        ),
    ]
