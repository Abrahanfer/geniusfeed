# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geniusfeed', '0003_auto_20150807_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeditem',
            name='feed',
            field=models.ForeignKey(to='geniusfeed.Feed', related_name='feed_items'),
        ),
    ]
