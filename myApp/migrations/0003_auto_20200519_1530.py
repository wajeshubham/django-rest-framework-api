# Generated by Django 3.0.5 on 2020-05-19 10:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_auto_20200519_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperiod',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 10, 0, 44, 506564, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='activityperiod',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 19, 10, 0, 44, 506564, tzinfo=utc)),
        ),
    ]