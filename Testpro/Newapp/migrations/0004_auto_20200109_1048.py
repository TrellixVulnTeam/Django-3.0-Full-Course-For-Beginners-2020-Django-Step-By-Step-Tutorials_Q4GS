# Generated by Django 3.0.2 on 2020-01-09 03:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Newapp', '0003_newsdb_pub_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsdb',
            name='pub_data',
            field=models.DateField(default=datetime.datetime(2020, 1, 9, 3, 47, 59, 953001, tzinfo=utc)),
        ),
    ]
