# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingDay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=2)),
                ('time', models.IntegerField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AddField(
            model_name='workingday',
            name='store',
            field=models.ForeignKey(to='home.Store'),
        ),
    ]
