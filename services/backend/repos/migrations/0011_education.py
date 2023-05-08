# Generated by Django 4.2 on 2023-04-13 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("repos", "0010_remove_role_organisation"),
    ]

    operations = [
        migrations.CreateModel(
            name="Education",
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
                ("start_date", models.DateTimeField(default=None, null=True)),
                ("end_date", models.DateTimeField(default=None, null=True)),
                ("grade", models.CharField(max_length=100)),
                ("institution", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
        ),
    ]