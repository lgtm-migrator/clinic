# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='HolidayWorking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'holiday date')),
                ('hour_8', models.IntegerField(default=-1)),
                ('hour_9', models.IntegerField(default=-1)),
                ('hour_10', models.IntegerField(default=-1)),
                ('hour_11', models.IntegerField(default=-1)),
                ('hour_12', models.IntegerField(default=-1)),
                ('hour_13', models.IntegerField(default=-1)),
                ('hour_14', models.IntegerField(default=-1)),
                ('hour_15', models.IntegerField(default=-1)),
                ('hour_16', models.IntegerField(default=-1)),
                ('hour_17', models.IntegerField(default=-1)),
                ('hour_18', models.IntegerField(default=-1)),
                ('hour_19', models.IntegerField(default=-1)),
                ('hour_20', models.IntegerField(default=-1)),
                ('hour_21', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'schedule date')),
                ('hour', models.IntegerField()),
                ('name', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('symptom', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Sortkey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('column1', models.CharField(max_length=25)),
                ('key1', models.CharField(max_length=25)),
                ('key2', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=254)),
                ('mail', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to=b'static/upload/')),
                ('access', models.TextField(max_length=500)),
                ('comment', models.TextField(max_length=500)),
                ('phone', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingDay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=2)),
                ('hour_8', models.IntegerField(default=-1)),
                ('hour_9', models.IntegerField(default=-1)),
                ('hour_10', models.IntegerField(default=-1)),
                ('hour_11', models.IntegerField(default=-1)),
                ('hour_12', models.IntegerField(default=-1)),
                ('hour_13', models.IntegerField(default=-1)),
                ('hour_14', models.IntegerField(default=-1)),
                ('hour_15', models.IntegerField(default=-1)),
                ('hour_16', models.IntegerField(default=-1)),
                ('hour_17', models.IntegerField(default=-1)),
                ('hour_18', models.IntegerField(default=-1)),
                ('hour_19', models.IntegerField(default=-1)),
                ('hour_20', models.IntegerField(default=-1)),
                ('hour_21', models.IntegerField(default=-1)),
                ('store', models.ForeignKey(to='home.Store')),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='store',
            field=models.ForeignKey(to='home.Store'),
        ),
        migrations.AddField(
            model_name='holidayworking',
            name='store',
            field=models.ForeignKey(to='home.Store'),
        ),
    ]
