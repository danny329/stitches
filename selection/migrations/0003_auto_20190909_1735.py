# Generated by Django 2.2.3 on 2019-09-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0002_auto_20190909_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='subtotal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]