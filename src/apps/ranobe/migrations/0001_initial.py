# Generated by Django 4.0.5 on 2022-06-29 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('compositions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ranobe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('composition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compositions.composition')),
            ],
        ),
    ]
