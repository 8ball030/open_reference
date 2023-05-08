"""
Simple views for the repos.
"""
from django.shortcuts import render

from .models import Repository, Tool, Language, Role, Organisation, Honor, Education




def repos(request):
    """Renders the repos page."""
    repos = Repository.objects.all().order_by("last_modified")
    return render(request, "repos.html", {"repos": reversed(repos)})


def tools(request):
    """Renders the tools page."""
    tools = Tool.objects.all()
    languages = Language.objects.all()
    return render(request, "tools.html", {"tools": tools, "languages": languages})


def roles(request):
    """Renders the roles page."""
    roles = Role.objects.all().order_by("end_date")
    return render(request, "roles.html", {"roles": roles})

def organisations(request):
    """Renders the organizations page."""
    organisation = Organisation.objects.all()
    return render(request, "organisations.html", {"organisations": organisation})


def home(request):
    """Renders the home page."""
    roles = Role.objects.all().order_by("end_date")
    organisations = Organisation.objects.all()
    tools = Tool.objects.all()
    languages = Language.objects.all()
    repos = Repository.objects.all().order_by("last_modified")
    honors = reversed(Honor.objects.all().order_by("date"))
    educations = reversed(Education.objects.all().order_by("start_date"))
    # for honor in honors:
    #     honor.date = honor.date.strftime("%B %Y")

    context = {
        "repos": reversed(repos),
        "tools": tools,
        "languages": languages,
        "roles": sorted(roles, key=lambda x: x.start_date, reverse=True),
        "organisations": organisations,
        "honors": honors,
        "educations": educations,
    }

    return render(request, "home.html", context)
