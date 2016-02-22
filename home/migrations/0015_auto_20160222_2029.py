# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20160222_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sortkey',
            name='key1',
            field=models.CharField(choices=[('store_id', 'Store Code'), ('region', 'Region'), ('nearest_station', 'Nearest Station')], max_length=25, default='region'),
        ),
        migrations.AlterField(
            model_name='sortkey',
            name='key2',
            field=models.CharField(choices=[('store_id', 'Store Code'), ('region', 'Region'), ('nearest_station', 'Nearest Station')], max_length=25, default='store_id'),
        ),
    ]
