from __future__ import unicode_literals

from django.db import models


class Tokens(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    token = models.CharField(max_length=100)
