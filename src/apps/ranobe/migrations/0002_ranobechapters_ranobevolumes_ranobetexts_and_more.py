# Generated by Django 4.0.5 on 2022-06-29 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ranobe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RanobeChapters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RanobeVolumes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('ranobe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranobe.ranobe')),
            ],
        ),
        migrations.CreateModel(
            name='RanobeTexts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('translation', models.CharField(max_length=120)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranobe.ranobechapters')),
            ],
        ),
        migrations.AddField(
            model_name='ranobechapters',
            name='volume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranobe.ranobevolumes'),
        ),
    ]
