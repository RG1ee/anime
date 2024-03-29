# Generated by Django 4.0.5 on 2022-06-29 20:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeSeasons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.anime')),
            ],
        ),
        migrations.CreateModel(
            name='AnimeSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.animeseasons')),
            ],
        ),
        migrations.CreateModel(
            name='AnimeVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='anime', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.animeseries')),
            ],
        ),
    ]
