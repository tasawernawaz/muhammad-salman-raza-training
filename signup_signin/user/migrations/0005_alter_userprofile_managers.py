# Generated by Django 4.2.4 on 2023-09-20 05:37

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0004_alter_userprofile_managers"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="userprofile",
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
