# Generated by Django 4.2.7 on 2023-11-30 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("equivalences", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="section",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="courses",
                to="equivalences.section",
            ),
        ),
        migrations.AlterField(
            model_name="program",
            name="university",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="programs",
                to="equivalences.university",
            ),
        ),
        migrations.AlterField(
            model_name="recognizedcourse",
            name="program",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recognized_courses",
                to="equivalences.program",
            ),
        ),
        migrations.AlterField(
            model_name="recognizedcourse",
            name="section",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recognized_courses",
                to="equivalences.section",
            ),
        ),
        migrations.AlterField(
            model_name="section",
            name="program",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sections",
                to="equivalences.program",
            ),
        ),
    ]
