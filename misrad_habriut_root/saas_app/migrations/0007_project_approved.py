# Generated by Django 4.1.2 on 2022-10-19 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saas_app', '0006_project_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Approved'),
        ),
    ]
