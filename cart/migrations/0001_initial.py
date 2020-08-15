# Generated by Django 3.0.8 on 2020-08-15 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food_delivery', '0005_auto_20200815_2155'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datePosted', models.DateTimeField(auto_now=True)),
                ('buyer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FoodInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('cartRef', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.Cart')),
                ('food', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='food_delivery.Food')),
            ],
        ),
    ]
