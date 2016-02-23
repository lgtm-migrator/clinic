# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20160223_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sortkey',
            name='key1',
            field=models.CharField(choices=[('store_id', 'Store Code'), ('region__code', 'Region'), ('nearest_station__code', 'Nearest Station')], max_length=25, default='region__code'),
        ),
        migrations.AlterField(
            model_name='sortkey',
            name='key2',
            field=models.CharField(choices=[('store_id', 'Store Code'), ('region__code', 'Region'), ('nearest_station__code', 'Nearest Station')], max_length=25, default='store_id'),
        ),
    ]
