# Generated by Django 4.0.5 on 2022-07-08 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0010_alter_manga_translation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='translation',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Continues'), (2, 'Frozen'), (3, 'Completed'), (4, 'Abondoned')], null=True, verbose_name='Translated status: '),
        ),
    ]
