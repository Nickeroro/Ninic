from django.conf import settings
from django.db import models
from django.utils import timezone


class pictures(models.Model):

    IMG_NAME = models.CharField(max_length=100, default='NONE')
    CATEGORY = models.CharField(max_length=100, default='NONE')
    IMG_URL = models.CharField(max_length=100, default='NONE')
    ALL = models.CharField(max_length=3, default='all')

    objects = models.Manager()
