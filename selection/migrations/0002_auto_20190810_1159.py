# Generated by Django 2.2.3 on 2019-08-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothmenu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
