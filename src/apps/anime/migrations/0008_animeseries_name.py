# Generated by Django 4.0.5 on 2022-07-05 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0007_alter_animevideo_options_remove_animeseries_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='animeseries',
            name='name',
            field=models.CharField(default=False, max_length=120, verbose_name='Series Name'),
        ),
    ]
