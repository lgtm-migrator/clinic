# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20160218_0351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='nearest_station',
        ),
        migrations.RemoveField(
            model_name='store',
            name='region',
        ),
    ]
