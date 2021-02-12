# Generated by Django 3.1.2 on 2020-12-16 17:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20201216_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerorders',
            name='order_id',
        ),
        migrations.AlterField(
            model_name='customerbooks',
            name='order_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.customerorders'),
        ),
        migrations.AlterField(
            model_name='customerorders',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 16, 23, 24, 34, 955275)),
        ),
        migrations.AlterField(
            model_name='order',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 16, 23, 24, 34, 954278)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 16, 23, 24, 34, 955275)),
        ),
    ]