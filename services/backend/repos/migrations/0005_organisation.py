# Generated by Django 4.2 on 2023-04-12 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("repos", "0004_add_tempory_data"),
    ]

    operations = [
        migrations.CreateModel(
            name="Organisation",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("url", models.URLField()),
                ("start_date", models.DateTimeField(default=None, null=True)),
                ("end_date", models.DateTimeField(default=None, null=True)),
            ],
        ),
    ]