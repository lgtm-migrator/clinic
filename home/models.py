from django.db import models

class Store(models.Model):
    id = models.CharField(max_length=200, unique=True, primary_key=True)
    name = models.CharField(max_length=200)
    mail = models.EmailField(max_length=200)
    image = models.ImageField(upload_to = 'static/upload/')
    access = models.TextField(max_length=500)
    comment = models.TextField(max_length=500)
    phone = models.IntegerField()
    created = models.DateTimeField('date created')
        
    def __str__(self):
        return self.name

    def get_store_code(self):
        return self.id

class WorkingDay(models.Model):
    store = models.ForeignKey(Store)
    type = models.CharField(max_length=2)
    time = models.IntegerField()

    def get_store_code(self):
        pass

class HolidayWorking(models.Model):
    store = models.ForeignKey(Store)
    date = models.DateField('holiday date')
    time = models.IntegerField()