# Generated by Django 4.2.11 on 2024-04-26 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('type', models.CharField(choices=[('rider', 'Rider'), ('driver', 'Driver')], max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
