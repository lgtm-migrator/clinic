# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20160218_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='store_id',
            field=models.CharField(default=1, unique=True, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='neareststation',
            name='code',
            field=models.CharField(unique=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='region',
            name='code',
            field=models.CharField(unique=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='store',
            name='id',
            field=models.AutoField(unique=True, serialize=False, primary_key=True),
        ),
        # migrations.AlterField(
        #     model_name='store',
        #     name='nearest_station',
        #     field=models.ForeignKey(to='home.NearestStation', null=True),
        # ),
        # migrations.AlterField(
        #     model_name='store',
        #     name='region',
        #     field=models.ForeignKey(to='home.Region', null=True),
        # ),
        migrations.AlterUniqueTogether(
            name='holidayworking',
            unique_together=set([('store', 'date')]),
        ),
        migrations.AlterUniqueTogether(
            name='workingday',
            unique_together=set([('store', 'type')]),
        ),
    ]
