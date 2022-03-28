# Generated by Django 3.1.5 on 2021-05-21 15:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cleverApp', '0003_category_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='property_address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 21, 15, 31, 27, 861683, tzinfo=utc)),
        ),
    ]
