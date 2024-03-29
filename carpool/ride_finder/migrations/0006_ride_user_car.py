# Generated by Django 4.2.5 on 2023-09-18 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_car_profile_phone_number_user_car"),
        (
            "ride_finder",
            "0005_remove_requeststatus_description_request_description_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="ride",
            name="user_car",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.user_car",
            ),
            preserve_default=False,
        ),
    ]
