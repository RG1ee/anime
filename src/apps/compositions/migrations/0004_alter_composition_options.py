# Generated by Django 4.0.5 on 2022-07-07 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compositions', '0003_rename_discription_composition_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='composition',
            options={'verbose_name_plural': 'Composition'},
        ),
    ]