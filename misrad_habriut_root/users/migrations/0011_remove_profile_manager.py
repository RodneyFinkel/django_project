# Generated by Django 4.0.7 on 2022-11-17 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_profile_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='manager',
        ),
    ]
