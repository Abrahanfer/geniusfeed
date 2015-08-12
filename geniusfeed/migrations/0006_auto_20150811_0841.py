# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geniusfeed', '0005_auto_20150811_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeditemread',
            name='fav',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='feeditemread',
            name='read',
            field=models.NullBooleanField(default=False),
        ),
    ]
