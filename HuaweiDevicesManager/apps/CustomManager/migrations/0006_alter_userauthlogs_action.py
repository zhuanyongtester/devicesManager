# Generated by Django 5.1.4 on 2024-12-23 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomManager', '0005_merge_20241223_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userauthlogs',
            name='action',
            field=models.CharField(choices=[('login', 'Login'), ('logout', 'Logout'), ('token', 'Token'), ('refresh', 'Refresh')], max_length=50, verbose_name='动作类型'),
        ),
    ]