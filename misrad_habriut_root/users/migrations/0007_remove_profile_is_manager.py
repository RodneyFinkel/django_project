# Generated by Django 3.2.16 on 2022-10-24 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_is_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_manager',
        ),
    ]
