# Generated by Django 4.0.5 on 2022-07-15 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_user_avatar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAvatar',
        ),
    ]
