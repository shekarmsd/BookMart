# Generated by Django 3.1.2 on 2020-12-11 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201211_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmart',
            name='book_price',
            field=models.FloatField(),
        ),
    ]
