# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_store_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
