# Generated by Django 4.2.4 on 2023-10-16 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_userprofile_id_alter_userprofile_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
