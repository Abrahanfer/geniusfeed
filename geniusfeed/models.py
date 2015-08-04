from django.db import models

class Feed(models.Model):
    title = models.CharField(max_length=200, blank=True, default='Default Title')
    link = models.URLField()# max_length=200 by default

class FeedItem(models.Model):
    feed = models.ForeignKey('Feed')
