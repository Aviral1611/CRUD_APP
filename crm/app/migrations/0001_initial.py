# Generated by Django 5.0.4 on 2024-10-02 18:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=20)),
                ("address", models.CharField(max_length=300)),
                ("city", models.CharField(max_length=200)),
                ("province", models.CharField(max_length=125)),
                ("country", models.CharField(max_length=125)),
            ],
        ),
    ]
