# Generated by Django 4.0.5 on 2022-07-22 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compositions', '0004_alter_composition_options'),
        ('ranobe', '0010_alter_ranobe_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranobe',
            name='composition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ranobe', to='compositions.composition', verbose_name='Composition'),
        ),
    ]
