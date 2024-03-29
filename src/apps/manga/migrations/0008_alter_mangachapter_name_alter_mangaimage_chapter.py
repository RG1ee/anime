# Generated by Django 4.0.5 on 2022-07-05 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0007_mangachapter_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mangachapter',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Chapter Title'),
        ),
        migrations.AlterField(
            model_name='mangaimage',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manga_images', to='manga.mangachapter', verbose_name='Manga Chapter'),
        ),
    ]
