# Generated by Django 5.0.6 on 2024-07-11 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_photo_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo_creator',
        ),
    ]
