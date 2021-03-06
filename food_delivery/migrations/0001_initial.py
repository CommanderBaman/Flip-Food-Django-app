# Generated by Django 3.0.8 on 2020-08-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='foods')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('available', models.BooleanField()),
            ],
        ),
    ]
