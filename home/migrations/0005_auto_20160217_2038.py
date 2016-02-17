# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20160217_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sortkey',
            name='key1',
            field=models.CharField(default=b'name', max_length=25, choices=[(b'name', b'Store name'), (b'phone', b'Phone number'), (b'mail', b'Email'), (b'region', b'region'), (b'nearest_station', b'Nearest Station')]),
        ),
        migrations.AlterField(
            model_name='sortkey',
            name='key2',
            field=models.CharField(default=b'phone', max_length=25, choices=[(b'name', b'Store name'), (b'phone', b'Phone number'), (b'mail', b'Email'), (b'region', b'region'), (b'nearest_station', b'Nearest Station')]),
        ),
        migrations.AlterField(
            model_name='sortkey',
            name='sorttype',
            field=models.CharField(default=b'001', unique=True, max_length=25, editable=False),
        ),
    ]
