# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20160223_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='有効な電話番号を入力してください。', code='invalid_phone', regex='^[0-9]+(-?[0-9]+)+$')]),
        ),
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='有効な電話番号を入力してください。', code='invalid_phone', regex='^[0-9]+(-?[0-9]+)+$')]),
        ),
    ]
