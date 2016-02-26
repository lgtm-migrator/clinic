# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20160223_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]+(-?[0-9]+)+$', message=b'\xe6\x9c\x89\xe5\x8a\xb9\xe3\x81\xaa\xe9\x9b\xbb\xe8\xa9\xb1\xe7\x95\xaa\xe5\x8f\xb7\xe3\x82\x92\xe5\x85\xa5\xe5\x8a\x9b\xe3\x81\x97\xe3\x81\xa6\xe3\x81\x8f\xe3\x81\xa0\xe3\x81\x95\xe3\x81\x84\xe3\x80\x82', code=b'invalid_phone')]),
        ),
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]+(-?[0-9]+)+$', message=b'\xe6\x9c\x89\xe5\x8a\xb9\xe3\x81\xaa\xe9\x9b\xbb\xe8\xa9\xb1\xe7\x95\xaa\xe5\x8f\xb7\xe3\x82\x92\xe5\x85\xa5\xe5\x8a\x9b\xe3\x81\x97\xe3\x81\xa6\xe3\x81\x8f\xe3\x81\xa0\xe3\x81\x95\xe3\x81\x84\xe3\x80\x82', code=b'invalid_phone')]),
        ),
    ]
