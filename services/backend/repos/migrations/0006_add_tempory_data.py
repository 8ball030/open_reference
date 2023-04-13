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



#
# def create_language(apps, schema_editor):
#     Language = apps.get_model("repos", "language")
#     Language.objects.create(
#         name=DEFAULT_LANGUAGE,
#         url=DEFAULT_LANGUAGE_URL,
#         description=DEFAULT_LANGUAGE_DESCRIPTION,
#     )

def create_role(apps, schema_editor):
    Role = apps.get_model("repos", "role")
    if not Role.objects.filter(name=DEFAULT_ROLE).exists():
        Role.objects.create(
            name=DEFAULT_ROLE,
            description=DEFAULT_ROLE_DESCRIPTION,
        )


def create_organization(apps, schema_editor):
    Organization = apps.get_model("repos", "organisation")
    organisations = [
        ("Valory.xyz", "https://valory.xyz", "Valory is a web3 startup dedicated to building the future of decentralized multi agent services"),
        ("Mobix", "https://mobix.io", "Mobix is a web3 startup dedicated to building the reducing carbon emissions through blockchain technology"),
        ("Datarella", "https://datarella.com", "Datarella is a web3 contracting company specialising in connecting data science and blockchain technology through partnerships with leading organisations such as Bosch, Tesla, and web3 startups such as Mobix."),
        ("Agent3", "https://agent3.io", "Agent3 is a marketing company specialising in providing targeted marketing solutions to large traditional technology institutions such as LinkedIn, Google and VMware."),
        ("Enable", "https://enable.com", "Enable is a SAAS company specialising in providing a platform for organisations to manage their digital assets. "),
        ("Santander", "https://santander.com", "Santander is a multinational banking and financial services company headquartered in Spain."),
        ("Barclays", "https://barclays.com", "Barclays is a British multinational investment bank and financial services company headquartered in London."),
    ]
    for organisation in organisations:
        if not Organization.objects.filter(name=organisation[0]).exists():
            Organization.objects.create(
            name=organisation[0],
            url=organisation[1],
            description=organisation[2],
        )
        else:
            # we merge the tool
            organisation_obj = Organization.objects.get(name=organisation[0])
            organisation_obj.url = organisation[1]
            organisation_obj.description = organisation[2]
            organisation_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ("repos", "0005_organisation"),

    ]

    operations = [
        # migrations.RunPython(create_author),
        # migrations.RunPython(create_owner),
        # migrations.RunPython(create_repos),
        # migrations.RunPython(create_language),
        migrations.RunPython(create_organization),
    ]
