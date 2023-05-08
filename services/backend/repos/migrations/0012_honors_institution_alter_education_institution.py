# Generated by Django 4.2 on 2023-04-13 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("repos", "0011_education"),
    ]

    operations = [
        migrations.CreateModel(
            name="Honors",
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
                ("issuer", models.CharField(max_length=100)),
                ("date", models.DateTimeField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Institution",
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
        migrations.AlterField(
            model_name="education",
            name="institution",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="repos.institution"
            ),
        ),
    ]