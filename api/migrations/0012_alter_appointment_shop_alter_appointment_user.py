# Generated by Django 4.2.9 on 2024-01-12 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0011_remove_appointment_shop_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="shop",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.shop"
            ),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.user"
            ),
        ),
    ]