# Generated by Django 4.2.11 on 2024-04-27 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rides', '0002_alter_ride_driver_alter_ride_rider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='rider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rides_as_rider', to=settings.AUTH_USER_MODEL),
        ),
    ]
