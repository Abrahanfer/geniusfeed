# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geniusfeed', '0004_auto_20150807_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeditemread',
            name='fav',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='feeditemread',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
