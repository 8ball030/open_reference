"""Definition of the initial models."""
from datetime import datetime

from django.db import models


class Author(models.Model):
    handle = models.CharField(max_length=100, unique=True, null=False, blank=False)


class Owner(models.Model):
    handle = models.CharField(max_length=100, unique=True, null=False, blank=False)


class Repository(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField(null=False, blank=False)
    last_modified = models.DateTimeField(default=None, null=True)
    last_checked = models.DateTimeField(default=None, null=True)


class Commit(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    sha = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class PullRequest(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.CharField(max_length=100)


class Language(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(null=False, blank=False)


class Tool(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(null=False, blank=False)
    description = models.TextField()


class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField(default=None, null=True)
    end_date = models.DateTimeField(default=None, null=True)


class Organisation(models.Model):
    """Represents an Organisation tht author and role can be associated with."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(null=False, blank=False)
    start_date = models.DateTimeField(default=None, null=True)
    end_date = models.DateTimeField(default=None, null=True)


class Honor(models.Model):
    """This is a data model to represent an honor."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    issuer = models.CharField(max_length=100)
    date = models.DateTimeField(default=None, null=True)


class Institution(models.Model):
    """Represents an educational institution."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(null=False, blank=False)
    start_date = models.DateTimeField(default=None, null=True)
    end_date = models.DateTimeField(default=None, null=True)


class Education(models.Model):
    """Represents an educational entry."""
    start_date = models.DateTimeField(default=None, null=True)
    end_date = models.DateTimeField(default=None, null=True)
    grade = models.CharField(max_length=100)
    degree = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
