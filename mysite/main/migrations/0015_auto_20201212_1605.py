# Generated by Django 3.1.2 on 2020-12-12 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0014_auto_20201212_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorders',
            name='books',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.bookmart'),
        ),
        migrations.AlterField(
            model_name='customerorders',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customerorders',
            name='payment_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.payment'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='books',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.bookmart'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.order'),
        ),
    ]
