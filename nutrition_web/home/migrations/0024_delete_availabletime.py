# Generated by Django 5.0.4 on 2024-04-08 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0023_rename_bkash_phone_sitedescription_bkash_phone_no_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="AvailableTime",
        ),
    ]
