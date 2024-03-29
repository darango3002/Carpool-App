# Generated by Django 4.2.5 on 2023-09-18 16:19

import address.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("address", "0003_auto_20200830_1851"),
        ("ride_finder", "0002_ride_destination_ride_start"),
    ]

    operations = [
        migrations.CreateModel(
            name="Request_Status",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("ACCEPTED", "Accepted"),
                            ("DENIED", "Denied"),
                            ("WAITING", "Waiting For Response"),
                        ],
                        default="WAITING",
                        max_length=8,
                    ),
                ),
                ("description", models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name="ride",
            name="seats",
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name="Request",
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
                (
                    "date_requested",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "pickup_location",
                    address.models.AddressField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="address.address",
                    ),
                ),
                (
                    "request_status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ride_finder.request_status",
                    ),
                ),
                (
                    "ride",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ride_finder.ride",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
