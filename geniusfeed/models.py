from django.db import models
from django.contrib.auth.models import User


class Feed(models.Model):
    title = models.CharField(max_length=200, blank=True,
                             default='Default Title Feed')
    link = models.URLField(default='http://localhost')# max_length=200
    # by default
    # Relationships
    users = models.ManyToManyField(User)

class FeedItem(models.Model):
    title = models.CharField(max_length=200, blank=True,
                             default='Default Title Feed Item')
    link = models.URLField(default='http://localhost')# max_length=200
    # by Default
    # Relationship
    feed = models.ForeignKey(Feed, related_name='feed_items')
    users = models.ManyToManyField(User, through='FeedItemRead')

class FeedItemRead(models.Model):
    feed_item = models.ForeignKey(FeedItem)
    user = models.ForeignKey(User)
    update_date = models.DateField()
    read = models.NullBooleanField(default=False)
    fav = models.NullBooleanField(default=False)
