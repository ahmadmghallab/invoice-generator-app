# Generated by Django 2.0.1 on 2018-11-09 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0021_auto_20181109_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='engine',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='license_plate',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='vin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
