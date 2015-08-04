# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200, blank=True, default='Default Title')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='FeedItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('feed', models.ForeignKey(to='geniusfeed.Feed')),
            ],
        ),
    ]
