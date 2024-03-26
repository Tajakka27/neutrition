# Generated by Django 5.0.3 on 2024-03-26 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0011_alter_appointment_time_delete_availabletime"),
    ]

    operations = [
        migrations.CreateModel(
            name="AvailableTime",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("day", models.CharField(max_length=20)),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
            ],
        ),
        migrations.AlterField(
            model_name="appointment",
            name="time",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="home.availabletime",
            ),
        ),
    ]
