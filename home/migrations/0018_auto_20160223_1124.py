# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20160223_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='phone',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='^[0-9]+(-[0-9]+)+?$', code='invalid_phone', message='Please enter a valid phone number')], max_length=15),
        ),
    ]
