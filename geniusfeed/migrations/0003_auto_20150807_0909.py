# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geniusfeed', '0002_feed_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedItemRead',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('update_date', models.DateField()),
                ('read', models.BooleanField()),
                ('fav', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='feeditem',
            name='link',
            field=models.URLField(default='http://localhost'),
        ),
        migrations.AddField(
            model_name='feeditem',
            name='title',
            field=models.CharField(default='Default Title Feed Item', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='feed',
            name='link',
            field=models.URLField(default='http://localhost'),
        ),
        migrations.AlterField(
            model_name='feed',
            name='title',
            field=models.CharField(default='Default Title Feed', max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='feeditemread',
            name='feed_item',
            field=models.ForeignKey(to='geniusfeed.FeedItem'),
        ),
        migrations.AddField(
            model_name='feeditemread',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feeditem',
            name='users',
            field=models.ManyToManyField(through='geniusfeed.FeedItemRead', to=settings.AUTH_USER_MODEL),
        ),
    ]
