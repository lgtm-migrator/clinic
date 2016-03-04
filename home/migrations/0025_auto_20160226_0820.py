# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_10',
            field=models.BooleanField(default=False, verbose_name='10'),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_11',
            field=models.BooleanField(default=False, verbose_name='11'),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_12',
            field=models.BooleanField(default=False, verbose_name='12'),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_13',
            field=models.BooleanField(default=False, verbose_name='13'),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_14',
            field=models.BooleanField(default=False, verbose_name='14'),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_15',
            field=models.BooleanField(default=False, verbose_name='15'),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_16',
            field=models.BooleanField(default=False, verbose_name='16'),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_17',
            field=models.BooleanField(default=False, verbose_name='17'),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_18',
            field=models.BooleanField(default=False, verbose_name='18'),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_19',
            field=models.BooleanField(default=False, verbose_name='19'),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_20',
            field=models.BooleanField(default=False, verbose_name='20'),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_21',
            field=models.BooleanField(default=False, verbose_name='21'),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_8',
            field=models.BooleanField(default=False, verbose_name='8'),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_9',
            field=models.BooleanField(default=False, verbose_name='9'),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='store',
            field=models.ForeignKey(verbose_name='Store', to='home.Store'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]+(-?[0-9]+)+$', message=b'\xe9\x9b\xbb\xe8\xa9\xb1\xe7\x95\xaa\xe5\x8f\xb7\xe3\x82\x92\xe6\xad\xa3\xe3\x81\x97\xe3\x81\x8f\xe5\x85\xa5\xe5\x8a\x9b\xe3\x81\x97\xe3\x81\xa6\xe3\x81\x8f\xe3\x81\xa0\xe3\x81\x95\xe3\x81\x84\xe3\x80\x82', code=b'invalid_phone')]),
        ),
        migrations.AlterField(
            model_name='store',
            name='access',
            field=models.TextField(max_length=500, verbose_name='\u30a2\u30af\u30bb\u30b9', blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='comment',
            field=models.TextField(max_length=500, verbose_name='\u304a\u5e97\u306e\u30b3\u30e1\u30f3\u30c8', blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='display',
            field=models.BooleanField(default=True, verbose_name='\u4e00\u89a7\u975e\u8868\u793a'),
        ),
        migrations.AlterField(
            model_name='store',
            name='image',
            field=models.ImageField(upload_to=b'static/upload/', verbose_name='\u5e97\u8217\u5199\u771f', blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='mail',
            field=models.EmailField(max_length=254, verbose_name='\u30e1\u30fc\u30eb\u30a2\u30c9\u30ec\u30b9'),
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.TextField(max_length=508, verbose_name='\u5e97\u8217\u540d'),
        ),
        migrations.AlterField(
            model_name='store',
            name='nearest_station',
            field=models.ForeignKey(blank=True, to='home.NearestStation', null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='\u96fb\u8a71\u756a\u53f7', validators=[django.core.validators.RegexValidator(regex=b'^[0-9]+(-?[0-9]+)+$', message=b'\xe9\x9b\xbb\xe8\xa9\xb1\xe7\x95\xaa\xe5\x8f\xb7\xe3\x82\x92\xe6\xad\xa3\xe3\x81\x97\xe3\x81\x8f\xe5\x85\xa5\xe5\x8a\x9b\xe3\x81\x97\xe3\x81\xa6\xe3\x81\x8f\xe3\x81\xa0\xe3\x81\x95\xe3\x81\x84\xe3\x80\x82', code=b'invalid_phone')]),
        ),
        migrations.AlterField(
            model_name='store',
            name='region',
            field=models.ForeignKey(blank=True, to='home.Region', null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_id',
            field=models.CharField(unique=True, max_length=254, verbose_name='Store Code'),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_10',
            field=models.BooleanField(default=False, verbose_name='10'),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_11',
            field=models.BooleanField(default=False, verbose_name='11'),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_12',
            field=models.BooleanField(default=False, verbose_name='12'),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_13',
            field=models.BooleanField(default=False, verbose_name='13'),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_14',
            field=models.BooleanField(default=False, verbose_name='14'),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_15',
            field=models.BooleanField(default=False, verbose_name='15'),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_16',
            field=models.BooleanField(default=False, verbose_name='16'),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_17',
            field=models.BooleanField(default=False, verbose_name='17'),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_18',
            field=models.BooleanField(default=False, verbose_name='18'),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_19',
            field=models.BooleanField(default=False, verbose_name='19'),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_20',
            field=models.BooleanField(default=False, verbose_name='20'),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_21',
            field=models.BooleanField(default=False, verbose_name='21'),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_8',
            field=models.BooleanField(default=False, verbose_name='8'),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_9',
            field=models.BooleanField(default=False, verbose_name='9'),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='type',
            field=models.CharField(max_length=2, verbose_name='Type', choices=[(b'Mo', '\u6708\u66dc\u65e5'), (b'Tu', '\u706b\u66dc\u65e5'), (b'We', '\u6c34\u66dc\u65e5'), (b'Th', '\u6728\u66dc\u65e5'), (b'Fr', '\u91d1\u66dc\u65e5'), (b'Sa', '\u571f\u66dc\u65e5'), (b'Su', '\u65e5\u66dc\u65e5'), (b'Ho', '\u795d\u796d\u65e5')]),
        ),
    ]
