from django.db import models

# Create your models here. we creat a table to change the name ,image,description
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class member(models.Model):
    nam=models.CharField(max_length=250)
    pic=models.ImageField(upload_to='photo')
    descr=models.TextField()