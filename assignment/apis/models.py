from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    Name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Artist(models.Model):
    Arname = models.CharField(max_length=100)
    Arwork = models.ManyToManyField('Work')

class Work(models.Model):
    YOUTUBE = 'YT'
    INSTAGRAM = 'IG'
    OTHER = 'OT'

    WORK_TYPE_OPTIONS = [
        (YOUTUBE, 'Youtube'),
        (INSTAGRAM, 'Instagram'),
        (OTHER, 'Other'),
    ]

    Link = models.URLField()
    Work_type = models.CharField(max_length=2, choices=WORK_TYPE_OPTIONS)
