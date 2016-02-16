# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_holidayworking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holidayworking',
            name='time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='store',
            name='id',
            field=models.CharField(max_length=200, unique=True, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='image',
            field=models.ImageField(default=b'upload/none/no-img.jpg', upload_to=b'upload/'),
        ),
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='time',
            field=models.IntegerField(),
        ),
    ]
