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
    display = models.BooleanField(default=True)

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
    
    hour_8 = models.BooleanField(default = False) # -1, 0, 1
    hour_9 = models.BooleanField(default = False)
    hour_10 = models.BooleanField(default = False)
    hour_11 = models.BooleanField(default = False)
    hour_12 = models.BooleanField(default = False)
    hour_13 = models.BooleanField(default = False)
    hour_14 = models.BooleanField(default = False)
    hour_15 = models.BooleanField(default = False)
    hour_16 = models.BooleanField(default = False)
    hour_17 = models.BooleanField(default = False)
    hour_18 = models.BooleanField(default = False)
    hour_19 = models.BooleanField(default = False)
    hour_20 = models.BooleanField(default = False)
    hour_21 = models.BooleanField(default = False)

    def is_dayoff(self,time_range):
        dayoff = True
        for i in time_range:
            if getattr(self, "hour_"+str(i)) == 1:
                return False
        return dayoff
    def __str__(self):
        return self.type
    class Meta:
        unique_together = (('store', 'type'), )

class HolidayWorking(models.Model):
    store = models.ForeignKey(Store)
    date = models.DateField('holiday date')

    hour_8 = models.BooleanField(default = False) # -1, 0, 1
    hour_9 = models.BooleanField(default = False)
    hour_10 = models.BooleanField(default = False)
    hour_11 = models.BooleanField(default = False)
    hour_12 = models.BooleanField(default = False)
    hour_13 = models.BooleanField(default = False)
    hour_14 = models.BooleanField(default = False)
    hour_15 = models.BooleanField(default = False)
    hour_16 = models.BooleanField(default = False)
    hour_17 = models.BooleanField(default = False)
    hour_18 = models.BooleanField(default = False)
    hour_19 = models.BooleanField(default = False)
    hour_20 = models.BooleanField(default = False)
    hour_21 = models.BooleanField(default = False)

    def is_dayoff(self,time_range):
        dayoff = True
        for i in time_range:
            if getattr(self, "hour_"+str(i)) == 1:
                return False
        return dayoff

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

class Holiday(models.Model):
    date = models.DateField('holiday')
    def __str__(self):
        return self.date.strftime("%d/%m/%Y")
