# Generated by Django 2.0.1 on 2018-11-07 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0015_auto_20181107_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='discount',
            field=models.FloatField(blank=True, default='0'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='qty',
            field=models.FloatField(blank=True, default='1'),
        ),
    ]
