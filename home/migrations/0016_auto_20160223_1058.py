# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20160222_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.CharField(validators=[django.core.validators.RegexValidator(code='invalid_phone', regex='^[0-9]+(-[0-9]+)+$', message='Please enter a valid phone number')], max_length=15),
        ),
    ]
