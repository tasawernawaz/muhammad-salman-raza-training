# Generated by Django 4.2.4 on 2023-10-13 11:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0003_alter_task_task_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="description",
            field=models.TextField(),
        ),
    ]