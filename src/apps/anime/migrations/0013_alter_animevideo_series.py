# Generated by Django 4.0.5 on 2022-07-22 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0012_alter_anime_composition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animevideo',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anime_videos', to='anime.animeseries', verbose_name='Anime Series'),
        ),
    ]
