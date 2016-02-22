# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20160220_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sortkey',
            name='key1',
            field=models.CharField(choices=[('store_id', 'Store Code'), ('region', 'region'), ('nearest_station', 'Nearest Station')], default='region', max_length=25),
        ),
        migrations.AlterField(
            model_name='sortkey',
            name='key2',
            field=models.CharField(choices=[('store_id', 'Store Code'), ('region', 'region'), ('nearest_station', 'Nearest Station')], default='store_id', max_length=25),
        ),
        migrations.AlterField(
            model_name='store',
            name='image',
            field=models.ImageField(upload_to='static/upload/'),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='type',
            field=models.CharField(choices=[('Mo', 'Monday'), ('Tu', 'Tuesday'), ('We', 'Webnesday'), ('Th', 'Thursday'), ('Fr', 'Friday'), ('Sa', 'Saturday'), ('Su', 'Sunday'), ('Ho', 'Holiday')], max_length=2),
        ),
    ]
