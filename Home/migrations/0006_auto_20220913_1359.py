# Generated by Django 2.2.19 on 2022-09-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_auto_20220913_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='Pizza_desc',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Pizza_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Pizza_price',
            field=models.FloatField(default=0),
        ),
    ]