# Generated by Django 4.0.5 on 2022-07-05 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0008_alter_mangachapter_name_alter_mangaimage_chapter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mangaimage',
            name='translation',
        ),
        migrations.AddField(
            model_name='manga',
            name='translation',
            field=models.CharField(blank=True, choices=[(1, 'Продолжается'), (2, 'Заморожен'), (3, 'Завершен'), (4, 'Заброшен')], max_length=120, null=True, verbose_name='Translated status: '),
        ),
    ]