# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workingday',
            name='type',
            field=models.CharField(max_length=2, choices=[(b'Mo', b'Monday'), (b'Tu', b'Tuesday'), (b'We', b'Webnesday'), (b'Th', b'Thursday'), (b'Fr', b'Friday'), (b'Sa', b'Saturday'), (b'Su', b'Sunday')]),
        ),
    ]
