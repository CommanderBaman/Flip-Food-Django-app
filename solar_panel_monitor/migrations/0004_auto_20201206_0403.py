# Generated by Django 3.1.4 on 2020-12-05 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solar_panel_monitor', '0003_auto_20201206_0334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailyvalue',
            old_name='Consumption',
            new_name='consumption',
        ),
        migrations.RenameField(
            model_name='dailyvalue',
            old_name='Solar Meter (Actual)',
            new_name='solar_meter_actual',
        ),
        migrations.RenameField(
            model_name='dailyvalue',
            old_name='Solar Meter (Company)',
            new_name='solar_meter_company',
        ),
    ]