# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20160216_1522'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Station',
            new_name='NearestStation',
        ),
        migrations.RenameModel(
            old_name='City',
            new_name='Region',
        ),
        migrations.RemoveField(
            model_name='sortkey',
            name='column1',
        ),
        migrations.AddField(
            model_name='sortkey',
            name='sorttype',
            field=models.CharField(default=1, max_length=25, editable=False),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together=set([('store', 'date', 'hour')]),
        ),
    ]
