# Generated by Django 4.2.7 on 2023-12-14 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("equivalences", "0009_equivalence_origin_program"),
    ]

    operations = [
        migrations.RenameField(
            model_name="equivalence",
            old_name="destination_course_name",
            new_name="destination_name",
        ),
        migrations.RenameField(
            model_name="equivalence",
            old_name="origin_program",
            new_name="destination_program",
        ),
        migrations.AlterField(
            model_name="equivalence",
            name="destination_university",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="equivalences_origin",
                to="equivalences.university",
            ),
        ),
        migrations.AlterField(
            model_name="equivalence",
            name="origin_university",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="equivalences_destination",
                to="equivalences.university",
            ),
        ),
    ]
