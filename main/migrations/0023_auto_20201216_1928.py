# Generated by Django 3.1.2 on 2020-12-16 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20201212_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordred',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
    ]
