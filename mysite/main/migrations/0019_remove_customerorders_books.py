# Generated by Django 3.1.2 on 2020-12-12 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_remove_customerbooks_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerorders',
            name='books',
        ),
    ]
