# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20160217_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='nearest_station',
            field=models.CharField(max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='store',
            name='region',
            field=models.CharField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='symptom',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='access',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='comment',
            field=models.TextField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='image',
            field=models.ImageField(upload_to=b'static/upload/', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='type',
            field=models.CharField(max_length=2, choices=[(b'Mo', b'Monday'), (b'Tu', b'Tuesday'), (b'We', b'Webnesday'), (b'Th', b'Thursday'), (b'Fr', b'Friday'), (b'Sa', b'Saturday'), (b'Su', b'Sunday'), (b'No', b'Holiday')]),
        ),
    ]
