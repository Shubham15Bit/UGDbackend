# Generated by Django 4.2.7 on 2023-12-07 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("equivalences", "0007_delete_subject"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studyplan",
            name="program",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="study_plans",
                to="equivalences.program",
            ),
        ),
    ]
