# Generated by Django 3.0.2 on 2021-01-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='city_name',
        ),
        migrations.RemoveField(
            model_name='city',
            name='city_value',
        ),
        migrations.AddField(
            model_name='city',
            name='latitude',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='city',
            name='longitude',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='city',
            name='name',
            field=models.CharField(default='Ghost', max_length=30),
        ),
        migrations.AddField(
            model_name='city',
            name='value',
            field=models.CharField(default='00', max_length=2),
        ),
    ]
