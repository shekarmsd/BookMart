# Generated by Django 3.1.2 on 2020-12-10 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201210_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmart',
            name='book_price',
            field=models.FloatField(null=True),
        ),
    ]