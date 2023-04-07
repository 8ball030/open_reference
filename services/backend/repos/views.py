"""
Simple views for the repos.
"""
from django.shortcuts import render

from .models import Repository, Tool, Language, Role


def home(request):
    """Renders the home page."""
    return render(request, "home.html")


def repos(request):
    """Renders the repos page."""
    repos = Repository.objects.all()
    return render(request, "repos.html", {"repos": repos})


def tools(request):
    """Renders the tools page."""
    tools = Tool.objects.all()
    languages = Language.objects.all()
    return render(request, "tools.html", {"tools": tools, "languages": languages})


def roles(request):
    """Renders the roles page."""
    roles = Role.objects.all()
    return render(request, "roles.html", {"roles": roles})
