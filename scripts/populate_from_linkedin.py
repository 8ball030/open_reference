"""
This is a simple script to populate the database with data from GitHub.
The script will create a new user for each GitHub user and a new project
for each GitHub repository. The script will also create a new commit for
each commit in the repository.

The script will also scrape the repository to find the programming languages
used in the repository. The script will then create a new language for each
programming language found in the repository.

The script will also scrape the repository to find the tools used in the
repository. The script will then create a new tool for each tool found in
the repository.

"""

import os
import sys
import json
from datetime import datetime
from time import sleep


import requests

from src.models import ReposAuthor as Author
from src.models import ReposOwner as Owner
from src.models import ReposCommit as Commit
from src.models import ReposRepository as Repository
from src.models import ReposLanguage as Language
from src.models import ReposTool as Tool
from src.models import ReposHonor
from src.models import ReposEducation
from src.models import ReposInstitution
from src.models import ReposOrganisation
from src.models import ReposRole

import pickle

import click
# we are using sqlalchemy to connect to the database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tqdm import tqdm

# we use the django sql lite database

engine = create_engine("sqlite:///services/backend/db.sqlite3")
Session = sessionmaker(bind=engine)
session = Session()


def get_linkedin(author_name):
    """Get the repositories for the GitHub user using requests."""
    file = open("object", "rb")
    profile = pickle.load(file)
    return profile


def add_if_not_found(session, model, **kwargs):
    """Add a new model to the database if it does not exist."""
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance

    instance = model(**kwargs)
    session.add(instance)
    session.commit()
    return instance

def parse_education_entry(entry):
    """Parse an educational entry from linked in order to create an output."""
    school = entry["schoolName"]
    degree = entry.get("degreeName", "NA")
    grade = entry.get("grade", "NA")
    # we get a date range, we want to get the start date
    description = entry.get("description", "NA")
    if "timePeriod" not in entry:
        return f"{school} - {degree} - {grade} - NA - NA"

    time_period = entry["timePeriod"]
    start_date = time_period.get("startDate", "NA")['year']
    start_date = datetime.strptime(str(start_date), '%Y')
    end_date = time_period.get("endDate", "NA")['year']
    end_date = datetime.strptime(str(end_date), '%Y')

    institution = add_if_not_found(session, ReposInstitution, name=school, description="N/a", url="N/a")

    edu = ReposEducation(
        institution=institution,
        degree=degree,
        grade=grade,
        start_date=start_date,
        end_date=end_date,
        description=description
    )
    return edu



def parse_honor_entry(entry):
    """
    Parse an honors entry from linked in order to create an output.
    honors: [{'description': 'Grand prize from Skale for a decentralised RPC', 'title': 'Eth Amsterdam', 'issueDate': {'month': 6, 'year': 2022}, 'issuer': 'Skale'}, {'description': 'Design and implementation of a custom trading strategy', 'occupation': 'urn:li:fs_education:(ACoAAAuaTzMB8WtSVfq24uaASoHn9HQeuhbOQ6Y,522977630)', 'title': 'First Prize at Quant Zone Rule Design', 'issueDate': {'month': 4, 'year': 2020}}, {'description': 'We implemented a parking simulator built on top of Fetch.ai in order to demonstrate negotiation and matchmaking in a decentralised system.', 'title': 'Winner of Diffusion Hackathon Track - Sharing in Consortia Networks: permissioned, tokenized data sharing with T-Labs', 'issueDate': {'month': 10, 'year': 2019}, 'issuer': 'Diffusion'}, {'description': 'Fetch is a tech stack allowing Agent based modelling. My winning entry involved reinforcement learning in an environment representing bartering for Music event tickets', 'title': 'Innovation Prize Hackathon 0x2', 'issueDate': {'month': 6, 'year': 2019}, 'issuer': 'Fetch.Ai'}, {'description': 'We implemented a parking simulator built on top of Fetch.ai in order to demonstrate negotiation and matchmaking in a decentralised system.', 'title': 'Diffusion Tech Stack Prize - Fetch.AI', 'issuer': 'Diffusion'}, {'description': 'We built a P2P ride sharing app. Built in python and Node.js', 'title': 'Hackathon 0x3 Decentralised Ride Sharing - First Prize', 'issuer': 'Fetch.Ai'}]

    """
    name = entry["title"]
    issuer = entry.get("issuer", "NA")
    date = entry.get("issueDate", "NA")
    if date != "NA":
        date = f"{date['month']}/{date['year']}"
        date = datetime.strptime(date, '%m/%Y')
    description = entry.get("description", "NA")

    return ReposHonor(
        name=name,
        issuer=issuer,
        date=date,
        description=description
    )


@click.command()
def analyse():
    """The main function."""
    # Get the GitHub username from the environment.
    profile = get_linkedin("author_name")

    click.echo("Adding education to the database")

    edus = []
    for education in tqdm(profile["education"][:2]):
        edu = parse_education_entry(education)
        edus.append(edu)
    [session.add(edu) for edu in edus]
    session.commit()

    click.echo("Adding honors to the database")
    honors = []
    for honor in tqdm(profile["honors"]):
        honor = parse_honor_entry(honor)
        honors.append(honor)
    [session.add(honor) for honor in honors]
    session.commit()

    # we now want to add the organizations
    click.echo("Adding organizations and experience to the database")
    orgs = []
    roles = []
    for exp in tqdm(profile["experience"]):
        org, experience = parse_experience(exp)
        orgs.append(org)
        roles.append(experience)

    [session.add(role) for role in roles]

    session.commit()


def parse_experience(exp):
    company_name = exp["companyName"]
    title = exp["title"]
    click.echo(f"Adding {title} to the database")
    description = exp.get("description", "NA")
    time_period = exp["timePeriod"]
    start_date = f"{time_period.get('startDate', 'NA')['year']}-{time_period.get('startDate', 'NA')['month']}"
    start_date = datetime.strptime(start_date, '%Y-%m')
    end_date = time_period.get('endDate', 'NA')
    if end_date == 'NA':
        end_date = None

    else:
        end_date = f"{end_date['year']}-{end_date['month']}"
        end_date = datetime.strptime(end_date, '%Y-%m')

    role = add_if_not_found(session, ReposRole, name=title, description=description, start_date=start_date, end_date=end_date)

    return "test", role





if __name__ == "__main__":
    analyse()
