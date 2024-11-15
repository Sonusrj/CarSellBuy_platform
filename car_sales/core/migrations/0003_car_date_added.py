# Generated by Django 5.1.3 on 2024-11-08 15:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_car_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
