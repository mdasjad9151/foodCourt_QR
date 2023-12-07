from django.db import models
import uuid

# Create your models here.
def qr():
    pass

class Owner(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4)
    name = models.CharField(max_length=200, default='')
    location =  models.CharField(max_length=500, default='')
    qr  =  models.ImageField(upload_to = 'image/QR', default= '')

    def __str__(self):
        return self.name
    

class Restaurants(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4)
    OwnerId =  models.ForeignKey(Owner, on_delete=models.CASCADE, default='')
    name =  models.CharField(max_length=100, default='')
    restro =  models.CharField(max_length=100, default= '')

class Menu(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4)
    rastroId = models.ForeignKey( Restaurants,on_delete=models.CASCADE, default='')
    desc =  models.CharField(max_length=300, default='')
    photo  =  models.ImageField(upload_to = 'image/restraurant', default =  '')