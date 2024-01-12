# Generated by Django 4.2.9 on 2024-01-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0009_alter_appointment_shop_alter_appointment_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="appointment",
            name="shop",
        ),
        migrations.RemoveField(
            model_name="appointment",
            name="user",
        ),
        migrations.AddField(
            model_name="appointment",
            name="shop_id",
            field=models.CharField(default="None", max_length=255),
        ),
        migrations.AddField(
            model_name="appointment",
            name="user_id",
            field=models.CharField(default="None", max_length=255),
        ),
    ]
