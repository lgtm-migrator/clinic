# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20160214_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='HolidayWorking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'holiday date')),
                ('time', models.IntegerField(max_length=200)),
                ('store', models.ForeignKey(to='home.Store')),
            ],
        ),
    ]
