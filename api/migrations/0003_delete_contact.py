# Generated by Django 4.2.9 on 2024-01-10 12:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_apppointment"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Contact",
        ),
    ]