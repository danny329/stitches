# Generated by Django 2.2.3 on 2019-07-30 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
