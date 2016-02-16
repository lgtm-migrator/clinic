# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('access', models.TextField(max_length=500)),
                ('comment', models.TextField(max_length=500)),
                ('mail', models.EmailField(max_length=200)),
                ('phone', models.IntegerField()),
                ('created', models.DateTimeField(verbose_name=b'date created')),
            ],
        ),
    ]
