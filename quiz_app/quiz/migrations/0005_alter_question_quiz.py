# Generated by Django 4.2.4 on 2023-10-23 06:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quiz", "0004_alter_options_question_alter_question_quiz"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="quiz",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="quiz.quiz",
            ),
        ),
    ]
