# Generated by Django 3.1.4 on 2020-12-05 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genCompany', models.FloatField()),
                ('genActual', models.FloatField()),
                ('consumption', models.FloatField()),
                ('dateRecorded', models.DateTimeField()),
            ],
        ),
    ]
