# Generated by Django 4.2.4 on 2023-10-24 10:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0005_alter_question_quiz"),
    ]

    operations = [
        migrations.AlterField(
            model_name="options",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="options",
                to="quiz.question",
            ),
        ),
    ]
