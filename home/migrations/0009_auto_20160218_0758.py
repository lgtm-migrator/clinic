# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20160218_0413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='holiday')),
            ],
        ),
        migrations.AlterField(
            model_name='holidayworking',
            name='date',
            field=models.DateField(verbose_name='holiday date'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateField(verbose_name='schedule date'),
        ),
        migrations.AlterField(
            model_name='sortkey',
            name='key1',
            field=models.CharField(max_length=25, choices=[('name', 'Store name'), ('phone', 'Phone number'), ('mail', 'Email'), ('region', 'region'), ('nearest_station', 'Nearest Station')], default='name'),
        ),
        migrations.AlterField(
            model_name='sortkey',
            name='key2',
            field=models.CharField(max_length=25, choices=[('name', 'Store name'), ('phone', 'Phone number'), ('mail', 'Email'), ('region', 'region'), ('nearest_station', 'Nearest Station')], default='phone'),
        ),
        migrations.AlterField(
            model_name='sortkey',
            name='sorttype',
            field=models.CharField(max_length=25, unique=True, default='001', editable=False),
        ),
        migrations.AlterField(
            model_name='store',
            name='image',
            field=models.ImageField(upload_to='static/upload/', blank=True),
        ),
        migrations.AlterField(
            model_name='workingday',
            name='type',
            field=models.CharField(max_length=2, choices=[('Mo', 'Monday'), ('Tu', 'Tuesday'), ('We', 'Webnesday'), ('Th', 'Thursday'), ('Fr', 'Friday'), ('Sa', 'Saturday'), ('Su', 'Sunday'), ('No', 'Holiday')]),
        ),
    ]
