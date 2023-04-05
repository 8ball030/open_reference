"""Definition of the initial models."""

from django.db import models

class Owner(models.Model):
    handle = models.CharField(max_length=100)

class Repository(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Commit(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    hash = models.CharField(max_length=100)
    message = models.TextField()

class PullRequest(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.CharField(max_length=100)

