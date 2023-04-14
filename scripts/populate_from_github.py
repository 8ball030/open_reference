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

import click
# we are using sqlalchemy to connect to the database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tqdm import tqdm

# we use the django sql lite database

engine = create_engine("sqlite:///services/backend/db.sqlite3")
Session = sessionmaker(bind=engine)
session = Session()


def get_repositories(author_name):
    """Get the repositories for the GitHub user using requests."""

    res = requests.get("https://api.github.com/users/{}/repos".format(author_name))
    if res.status_code != 200:
        raise Exception("Could not get repositories for user {}".format(author_name))

    repositories = res.json()
    click.echo("Found {} repositories for user {}".format(len(repositories), author_name))

    return repositories



def add_if_not_found(session, model, **kwargs):
    """Add a new model to the database if it does not exist."""
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance

    instance = model(**kwargs)
    session.add(instance)
    session.commit()
    return instance


@click.command()
def analyse():
    """The main function."""
    # Get the GitHub username from the environment.
    author_name = "8ball030"

    repositories = get_repositories(author_name)
    # Get the repositories for the GitHub user.
    # for repository in tqdm(repositories):
    #     # we get the name of the repository
    #     # we get the owner of the repository
    #     owner = add_if_not_found(session, Owner, handle=repository["owner"]["login"])
    #     author = add_if_not_found(session, Author, handle=author_name)
    #     last_commit = repository["updated_at"]
    #     last_modified = repository["pushed_at"]
    #     last_modified = datetime.strptime(last_modified, '%Y-%m-%dT%H:%M:%SZ')
    #     last_checked = datetime.now()
    #     name = repository["name"]
    #     url = repository["html_url"]
    #     if not (repo := session.query(Repository).filter_by(name=name).first()):
    #         new_repository = Repository(
    #             name=name,
    #             url=url,
    #             last_modified=last_modified,
    #             last_checked=last_checked,
    #             author=author,
    #             owner=owner
    #         )
    #         session.add(new_repository)
    #         click.echo("Added repository {} to the database".format(name))
    #     else:
    #         repo.last_modified = last_modified
    #         repo.last_checked = last_checked
    #         repo.author = author
    #         repo.owner = owner
    #         click.echo("Updated repository {} in the database".format(name))
    #     sleep(1)
    # session.commit()
    # # now we have our repositories
    # # we need to get the commits for each repository
    # # we need to get the programming languages for each repository
    # # we need to get the tools for each repository
    # # we need to get the roles for each repository
    # repos = session.query(Repository).all()
    # for repo in tqdm(repos):
    #     commits = requests.get("https://api.github.com/repos/{}/{}/commits".format(repo.owner.handle, repo.name))
    #     if commits.status_code != 200:
    #         click.echo("Could not get commits for repository {}".format(repo.name))
    #         continue
    #     commits = commits.json()
    #     for commit in commits:
    #         sha = commit["sha"]
    #         if not (commit_model := session.query(Commit).filter_by(sha=sha).first()):
    #             if commit["author"] is None or commit["author"]["login"] is None:
    #                 author = add_if_not_found(session, Author, handle="Unknown")
    #             else:
    #                 author = add_if_not_found(session, Author, handle=commit["author"]["login"])

    #             new_commit = Commit(
    #                 sha=sha,
    #                 repository=repo,
    #                 message=commit["commit"]["message"],
    #                 date=datetime.strptime(commit["commit"]["author"]["date"], '%Y-%m-%dT%H:%M:%SZ'),
    #                 author=author
    #             )
    #             session.add(new_commit)
    #             click.echo("Added commit {} to the database".format(sha))
    #         else:
    #             commit_model.repository = repo
    #             click.echo("Updated commit {} in the database".format(sha))
    #         sleep(1)
    # session.commit()


    # # now we have our commits
    # # we need to get the programming languages for each repository
    # # we need to get the tools for each repository
    # # we need to get the roles for each repository

    repos = session.query(Repository).all()
    for repo in tqdm(repos):
        languages = requests.get("https://api.github.com/repos/{}/{}/languages".format(repo.owner.handle, repo.name))
        if languages.status_code != 200:
            click.echo("Could not get languages for repository {}".format(repo.name))
            continue
        languages = languages.json()
        for language in languages:
            if not (language_model := session.query(Language).filter_by(name=language).first()):
                new_language = Language(
                    name=language,
                    description="Scraped from GitHub.",
                    url="https://api.github.com/repos/{}/{}/languages".format(repo.owner.handle, repo.name)
                )
                session.add(new_language)
                click.echo("Added language {} to the database".format(language))
            else:
                click.echo("Language {} already in the database".format(language))
            sleep(1)

    session.commit()

    # now we have our languages
    # we need to get the tools for each repository
    # we will use the GitHub API to get the tools

    repos = session.query(Repository).all()
    for repo in tqdm(repos):
        tools = requests.get("https://api.github.com/repos/{}/{}/topics".format(repo.owner.handle, repo.name))
        if tools.status_code != 200:
            click.echo("Could not get tools for repository {}".format(repo.name))
            continue
        tools = tools.json()
        for tool in tools["names"]:
            if not (tool_model := session.query(Tool).filter_by(name=tool).first()):
                new_tool = Tool(
                    name=tool,
                    description="Scraped from GitHub.",
                    url="https://api.github.com/repos/{}/{}/topics".format(repo.owner.handle, repo.name)
                )
                session.add(new_tool)
                click.echo("Added tool {} to the database".format(tool))
            else:
                click.echo("Tool {} already in the database".format(tool))
            sleep(1)






# we use click
if __name__ == "__main__":
    analyse()
