# Generated by Django 4.2.16 on 2024-12-16 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserLogin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='token',
            table='t_admin_token',
        ),
    ]
