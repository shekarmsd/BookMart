# Generated by Django 3.1.2 on 2020-12-16 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20201216_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 16, 20, 12, 34, 250163)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 16, 20, 12, 34, 251677)),
        ),
    ]