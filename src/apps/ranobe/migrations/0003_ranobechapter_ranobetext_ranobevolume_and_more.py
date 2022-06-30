# Generated by Django 4.0.5 on 2022-06-30 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compositions', '0002_alter_composition_discription_and_more'),
        ('ranobe', '0002_ranobechapters_ranobevolumes_ranobetexts_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RanobeChapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Chapter Number')),
                ('name', models.CharField(max_length=120, verbose_name='Chapter Title')),
                ('description', models.TextField(verbose_name='Chapter Description')),
            ],
        ),
        migrations.CreateModel(
            name='RanobeText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Ranobe Text')),
                ('translation', models.CharField(max_length=120, verbose_name='Translated by: ')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranobe.ranobechapter', verbose_name='Ranobe Chapter')),
            ],
        ),
        migrations.CreateModel(
            name='RanobeVolume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Volume Name')),
            ],
        ),
        migrations.RemoveField(
            model_name='ranobetexts',
            name='chapter',
        ),
        migrations.RemoveField(
            model_name='ranobevolumes',
            name='ranobe',
        ),
        migrations.AlterField(
            model_name='ranobe',
            name='composition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compositions.composition', verbose_name='Composition'),
        ),
        migrations.DeleteModel(
            name='RanobeChapters',
        ),
        migrations.DeleteModel(
            name='RanobeTexts',
        ),
        migrations.DeleteModel(
            name='RanobeVolumes',
        ),
        migrations.AddField(
            model_name='ranobevolume',
            name='ranobe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranobe.ranobe', verbose_name='Ranobe'),
        ),
        migrations.AddField(
            model_name='ranobechapter',
            name='volume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranobe.ranobevolume', verbose_name='Ranobe Volume'),
        ),
    ]
