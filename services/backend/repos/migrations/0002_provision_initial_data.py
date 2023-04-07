# Generated by Django 4.2 on 2023-04-07 10:13
from datetime import datetime

from django.db import migrations
from repos.constants import (
    DEFAULT_AUTHOR,
    DEFAULT_REPO_NAME,
    DEFAULT_OWNER,
    DEFAULT_REPO_URL,
    DEFAULT_TOOL,
    DEFAULT_TOOL_URL,
    DEFAULT_LANGUAGE,
    DEFAULT_LANGUAGE_URL,
    DEFAULT_TOOL_DESCRIPTION,
    DEFAULT_LANGUAGE_DESCRIPTION,
    DEFAULT_ROLE,
    DEFAULT_ROLE_DESCRIPTION,
)


def create_author(apps, schema_editor):
    Author = apps.get_model("repos", "author")
    Author.objects.create(
        handle=DEFAULT_AUTHOR,
    )


def create_owner(apps, schema_editor):
    Owner = apps.get_model("repos", "owner")
    Owner.objects.create(
        handle=DEFAULT_OWNER,
    )


def create_repos(apps, schema_editor):
    # we now get the author
    Author = apps.get_model("repos", "author")
    author = Author.objects.get(handle=DEFAULT_AUTHOR)

    # we now get the owner
    Owner = apps.get_model("repos", "owner")
    owner = Owner.objects.get(handle=DEFAULT_OWNER)

    Repo = apps.get_model("repos", "repository")
    Repo.objects.create(
        name=DEFAULT_REPO_NAME,
        url=DEFAULT_REPO_URL,
        owner=owner,
        author=author,
        last_modified=datetime.now(),
        last_checked=datetime.now(),
    )


def create_tool(apps, schema_editor):
    Tool = apps.get_model("repos", "tool")
    Tool.objects.create(
        name=DEFAULT_TOOL,
        url=DEFAULT_TOOL_URL,
        description=DEFAULT_TOOL_DESCRIPTION,
    )


def create_language(apps, schema_editor):
    Language = apps.get_model("repos", "language")
    Language.objects.create(
        name=DEFAULT_LANGUAGE,
        url=DEFAULT_LANGUAGE_URL,
        description=DEFAULT_LANGUAGE_DESCRIPTION,
    )


def create_role(apps, schema_editor):
    Role = apps.get_model("repos", "role")
    Role.objects.create(
        name=DEFAULT_ROLE,
        description=DEFAULT_ROLE_DESCRIPTION,
    )


class Migration(migrations.Migration):

    dependencies = [
        ("repos", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_author),
        migrations.RunPython(create_owner),
        migrations.RunPython(create_repos),
        migrations.RunPython(create_tool),
        migrations.RunPython(create_language),
        migrations.RunPython(create_role),
    ]