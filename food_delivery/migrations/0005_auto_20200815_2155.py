# Generated by Django 3.0.8 on 2020-08-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_delivery', '0004_auto_20200813_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='ingredients',
            field=models.TextField(default='Details not provided by Chef'),
        ),
    ]
