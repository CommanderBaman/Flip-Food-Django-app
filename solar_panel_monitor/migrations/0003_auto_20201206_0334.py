# Generated by Django 3.1.4 on 2020-12-05 22:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('solar_panel_monitor', '0002_auto_20201206_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyvalue',
            name='dateRecorded',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
