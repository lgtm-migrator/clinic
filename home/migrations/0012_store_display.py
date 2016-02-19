# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20160219_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='display',
            field=models.BooleanField(default=True),
        ),
    ]
