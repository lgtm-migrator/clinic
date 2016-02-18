# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20160218_0413'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='nearest_station',
            field=models.ForeignKey(to='home.NearestStation', null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='region',
            field=models.ForeignKey(to='home.Region', null=True),
        ),
    ]
