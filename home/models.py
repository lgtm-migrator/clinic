# -*- coding: utf-8 -*-
from django.db import models

# # 地域テーブル
class Region(models.Model):
    code = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

# # 最寄り駅テーブル
class NearestStation(models.Model):
    code = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

# ソートキーテーブル
SORT_KEY = (('name', 'Store name'), ('phone', 'Phone number'), ('mail', 'Email'), ('region', 'region'), ('nearest_station', 'Nearest Station'));
class Sortkey(models.Model):
    sorttype = models.CharField(default='001', max_length=25, editable=False, unique=True)
    key1 = models.CharField(max_length=25, choices= SORT_KEY, default='name')
    key2 = models.CharField(max_length=25, choices=SORT_KEY, default='phone')

    def __str__(self):
        return 'Sort key. Click to edit'

class Store(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    store_id = models.CharField(max_length=254, unique=True)
    name = models.CharField(max_length=254)
    phone = models.IntegerField()
    mail = models.EmailField()
    image = models.ImageField(upload_to = 'static/upload/', blank=True)
    
    access = models.TextField(max_length=500, blank=True)
    comment = models.TextField(max_length=500, blank=True)
    
    region = models.ForeignKey(Region, null=True)
    nearest_station = models.ForeignKey(NearestStation, null=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_store_code(self):
        return self.store_id

WORKING_DAY = (
    ('Mo', 'Monday'),
    ('Tu', 'Tuesday'),
    ('We', 'Webnesday'),
    ('Th', 'Thursday'),
    ('Fr', 'Friday'),
    ('Sa', 'Saturday'),
    ('Su', 'Sunday'),
    ('No', 'Holiday')
)

class WorkingDay(models.Model):
    store = models.ForeignKey(Store)
    type = models.CharField(max_length=2, choices=WORKING_DAY)

    hour_8 = models.IntegerField(default = -1) # -1, 0, 1
    hour_9 = models.IntegerField(default = -1)
    hour_10 = models.IntegerField(default = -1)
    hour_11 = models.IntegerField(default = -1)
    hour_12 = models.IntegerField(default = -1)
    hour_13 = models.IntegerField(default = -1)
    hour_14 = models.IntegerField(default = -1)
    hour_15 = models.IntegerField(default = -1)
    hour_16 = models.IntegerField(default = -1)
    hour_17 = models.IntegerField(default = -1)
    hour_18 = models.IntegerField(default = -1)
    hour_19 = models.IntegerField(default = -1)
    hour_20 = models.IntegerField(default = -1)
    hour_21 = models.IntegerField(default = -1)

    class Meta:
        unique_together = (('store', 'type'), )

class HolidayWorking(models.Model):
    store = models.ForeignKey(Store)
    date = models.DateField('holiday date')

    hour_8 = models.IntegerField(default = -1) # -1, 0, 1
    hour_9 = models.IntegerField(default = -1)
    hour_10 = models.IntegerField(default = -1)
    hour_11 = models.IntegerField(default = -1)
    hour_12 = models.IntegerField(default = -1)
    hour_13 = models.IntegerField(default = -1)
    hour_14 = models.IntegerField(default = -1)
    hour_15 = models.IntegerField(default = -1)
    hour_16 = models.IntegerField(default = -1)
    hour_17 = models.IntegerField(default = -1)
    hour_18 = models.IntegerField(default = -1)
    hour_19 = models.IntegerField(default = -1)
    hour_20 = models.IntegerField(default = -1)
    hour_21 = models.IntegerField(default = -1)

    class Meta:
        unique_together = (('store', 'date'), )

class Schedule(models.Model):
    store = models.ForeignKey(Store)
    date = models.DateField('schedule date')
    hour = models.IntegerField()
    name = models.CharField(max_length=254)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    symptom = models.TextField(max_length=500, blank=True)

    class Meta:
        unique_together = (('store', 'date', 'hour'), )