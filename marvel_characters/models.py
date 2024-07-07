from django.db import models

# Create your models here.

class CharacterProfile(models.Model):
    char = models.CharField(max_length=50, blank=True)
    charname = models.CharField(max_length=200, blank=True)
    birthname = models.CharField(max_length=200, blank=True)
    types = models.CharField(max_length=200, blank=True)
    universes = models.CharField(max_length=200, blank=True)
    birthplace = models.CharField(max_length=200, blank=True)
    superpowers = models.CharField(max_length=200, blank=True)
    religions = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=200, blank=True)
    occupation = models.CharField(max_length=200, blank=True)
    memberof = models.CharField(max_length=200, blank=True)