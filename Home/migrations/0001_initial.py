# Generated by Django 2.2.19 on 2022-09-09 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('Pizza_name', models.CharField(max_length=100)),
                ('Pizza_desc', models.TextField(max_length=100)),
                ('Pizza_price', models.FloatField(max_length=100)),
                ('image_url', models.URLField(default='')),
            ],
        ),
    ]
