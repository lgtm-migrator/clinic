from django.db import models

class City(models.Model):
    code = models.CharField(max_length=25)
    name = models.CharField(max_length=254)

class Station(models.Model):
    code = models.CharField(max_length=25)
    name = models.CharField(max_length=254)

class Sortkey(models.Model):
    column1 = models.CharField(max_length=25)
    key1 = models.CharField(max_length=25)
    key2 = models.CharField(max_length=25)

class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)
    mail = models.EmailField()
    image = models.ImageField(upload_to = 'static/upload/')
    access = models.TextField(max_length=500)
    comment = models.TextField(max_length=500)
    phone = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.name

    def get_store_code(self):
        return self.id

class WorkingDay(models.Model):
    store = models.ForeignKey(Store)
    type = models.CharField(max_length=2)

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

    def get_store_code(self):
        pass

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

class Schedule(models.Model):
    store = models.ForeignKey(Store)
    date = models.DateField('schedule date')
    hour = models.IntegerField()
    name = models.CharField(max_length=254)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    email = models.EmailField()
    symptom = models.TextField(max_length=500)