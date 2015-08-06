from django.db import models
from django.contrib.auth.models import User


class Feed(models.Model):
    title = models.CharField(max_length=200, blank=True, default='Default Title')
    link = models.URLField()# max_length=200 by default
    # Relationships
    users = models.ManyToManyField(User)

class FeedItem(models.Model):
    feed = models.ForeignKey('Feed')
