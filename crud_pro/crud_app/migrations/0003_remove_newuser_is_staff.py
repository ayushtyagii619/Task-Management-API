# Generated by Django 5.0.6 on 2024-10-11 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0002_newuser_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='is_staff',
        ),
    ]
