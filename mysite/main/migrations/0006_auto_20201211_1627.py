# Generated by Django 3.1.2 on 2020-12-11 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201211_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='peoduct',
        ),
        migrations.RemoveField(
            model_name='transectiondetails',
            name='peoduct',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
