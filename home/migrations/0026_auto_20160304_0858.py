# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20160304_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_10',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='10', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_11',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='11', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_12',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='12', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_13',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='13', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_14',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='14', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_15',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='15', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_16',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='16', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_17',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='17', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_18',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='18', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_19',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='19', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_20',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='20', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_21',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='21', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_8',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='8', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_9',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='9', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='store',
            field=models.ForeignKey(to='home.Store', verbose_name='Store'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='phone',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='電話番号を正しく入力してください。', code='invalid_phone', regex='^[0-9]+(-?[0-9]+)+$')], max_length=15),
        ),
        migrations.AlterField(
            model_name='store',
            name='access',
            field=models.TextField(max_length=500, verbose_name='アクセス', blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='comment',
            field=models.TextField(max_length=500, verbose_name='お店のコメント', blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='display',
            field=models.BooleanField(default=True, verbose_name='一覧非表示'),
        ),
        migrations.AlterField(
            model_name='store',
            name='image',
            field=models.ImageField(upload_to='static/upload/', verbose_name='店舗写真', blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='mail',
            field=models.EmailField(validators=[django.core.validators.EmailValidator(message='メールアドレスを正しく入力してください。')], max_length=254, verbose_name='メールアドレス'),
        ),
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(1)], max_length=508, verbose_name='店舗名'),
        ),
        migrations.AlterField(
            model_name='store',
            name='nearest_station',
            field=models.ForeignKey(null=True, blank=True, to='home.NearestStation'),
        ),
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='電話番号を正しく入力してください。', code='invalid_phone', regex='^[0-9]+(-?[0-9]+)+$')], max_length=15, verbose_name='電話番号'),
        ),
        migrations.AlterField(
            model_name='store',
            name='region',
            field=models.ForeignKey(null=True, blank=True, to='home.Region'),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_id',
            field=models.CharField(validators=[django.core.validators.MinLengthValidator(1)], unique=True, max_length=254, verbose_name='Store Code'),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_10',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='10', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_11',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='11', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_12',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='12', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_13',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='13', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_14',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='14', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_15',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='15', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_16',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='16', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_17',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='17', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_18',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='18', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_19',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='19', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_20',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='20', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_21',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='21', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_8',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='8', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_9',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)], null=True, verbose_name='9', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='type',
            field=models.CharField(choices=[('Mo', '月曜日'), ('Tu', '火曜日'), ('We', '水曜日'), ('Th', '木曜日'), ('Fr', '金曜日'), ('Sa', '土曜日'), ('Su', '日曜日'), ('Ho', '祝祭日')], max_length=2, verbose_name='営業時間帯'),
        ),
    ]
