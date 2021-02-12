# Generated by Django 3.1.2 on 2020-12-16 14:46

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20201216_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerorders',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='customerorders',
            name='date_added',
        ),
        migrations.AddField(
            model_name='customerorders',
            name='date_ordred',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customerorders',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 16, 20, 16, 12, 683465)),
        ),
        migrations.AddField(
            model_name='customerorders',
            name='package',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 16, 20, 16, 12, 678488)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 16, 20, 16, 12, 680639)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
    ]
