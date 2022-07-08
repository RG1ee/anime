# Generated by Django 4.0.5 on 2022-07-07 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ranobe', '0007_ranobe_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ranobechapter',
            options={'verbose_name_plural': 'Ranobe Chapter'},
        ),
        migrations.AlterModelOptions(
            name='ranobetext',
            options={'verbose_name_plural': 'Ranobe Text'},
        ),
        migrations.AlterModelOptions(
            name='ranobevolume',
            options={'verbose_name_plural': 'Ranobe Volume'},
        ),
        migrations.AlterField(
            model_name='ranobechapter',
            name='volume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ranobe_chapters', to='ranobe.ranobevolume', verbose_name='Ranobe Volume'),
        ),
    ]