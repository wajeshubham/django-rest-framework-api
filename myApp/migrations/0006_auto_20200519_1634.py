# Generated by Django 3.0.5 on 2020-05-19 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_auto_20200519_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperiod',
            name='end_time',
            field=models.DateTimeField(default='2020-05-19 11:04'),
        ),
        migrations.AlterField(
            model_name='activityperiod',
            name='start_time',
            field=models.DateTimeField(default='2020-05-19 11:04'),
        ),
    ]