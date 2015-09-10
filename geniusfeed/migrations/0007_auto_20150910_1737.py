# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.contrib.auth.hashers import make_password

def load_initial_data(apps, schema_editor):
    """
    Populate the DB with test data
    """
    # Get User model
    User = apps.get_model("auth", "User")
    # Create three test users for feeds
    test_user_1 = User.objects.create(username="test-user-1",
                                      first_name="User 1",
                                      last_name="Tester",
                                      email="test-user-1@nowhere.com",
                                      password=make_password("test1"))
    test_user_2 = User.objects.create(username="test-user-2",
                                      first_name="User 2",
                                      last_name="Tester",
                                      email="test-user-2@nowhere.com",
                                      password=make_password("test2"))
    test_user_3 = User.objects.create(username="test-user-3",
                                      first_name="User 3",
                                      last_name="Tester",
                                      email="test-user-3@nowhere.com",
                                      password=make_password("test3"))

    Feed = apps.get_model("geniusfeed", "Feed")
    # Create 5 Feeds
    test_feed_1 = Feed.objects.create(title="Test Feed 1",
                                      link="http://localhost")
    # QuerySet = User.objects.filter(username="test_feed_1")
    # test_feed_1.users =  QuerySet(test_user_1, test_user_2)

def reverse_load_initial_data(apps, schema_editor):
    """
    Remove all test data from DB
    """
    User = apps.get_model("auth", "User")
    test_users = User.objects.filter(username__startswith='test-user-')
    test_users.delete()

    Feed = apps.get_model("geniusfeed", "Feed")
    test_feeds = Feed.objects.filter(title__startswith='test-feed-')
    test_feeds.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('geniusfeed', '0006_auto_20150811_0841'),

    ]

    operations = [
        migrations.RunPython(load_initial_data)
    ]
