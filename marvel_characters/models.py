from django.db import models

# Create your models here.

class CharacterProfile(models.Model):
    char = models.CharField(max_length=200, blank=True)
    charname = models.CharField(max_length=200, blank=True)
    birthname = models.CharField(max_length=200, blank=True)
    types = models.JSONField(default=list, blank=True)
    universes = models.JSONField(default=list, blank=True)
    birthplace = models.CharField(max_length=200, blank=True)
    superpowers = models.JSONField(default=list, blank=True)
    religions = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=200, blank=True)
    occupation = models.JSONField(default=list, blank=True)
    memberof = models.JSONField(default=list, blank=True)