# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20160304_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_10',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='10', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_11',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='11', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_12',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='12', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_13',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='13', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_14',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='14', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_15',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='15', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_16',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='16', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_17',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='17', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_18',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='18', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_19',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='19', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_20',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='20', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_21',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='21', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_8',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='8', blank=True),
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='hour_9',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='9', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_10',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='10', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_11',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='11', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_12',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='12', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_13',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='13', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_14',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='14', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_15',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='15', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_16',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='16', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_17',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='17', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_18',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='18', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_19',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='19', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_20',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='20', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_21',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='21', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_8',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='8', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='hour_9',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99, '枠を正しく入力してください。'), django.core.validators.MinValueValidator(0, '枠を正しく入力してください。')], verbose_name='9', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together=set([]),
        ),
    ]
