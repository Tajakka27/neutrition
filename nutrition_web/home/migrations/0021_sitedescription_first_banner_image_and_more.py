# Generated by Django 5.0.3 on 2024-03-31 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0020_rename_concerns_appointment_cause"),
    ]

    operations = [
        migrations.AddField(
            model_name="sitedescription",
            name="First_banner_image",
            field=models.ImageField(blank=True, null=True, upload_to="banner_images"),
        ),
        migrations.AddField(
            model_name="sitedescription",
            name="Second_banner_image",
            field=models.ImageField(blank=True, null=True, upload_to="banner_images"),
        ),
        migrations.AddField(
            model_name="sitedescription",
            name="Third_banner_image",
            field=models.ImageField(blank=True, null=True, upload_to="banner_images"),
        ),
    ]
