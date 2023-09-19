from django.db import models

# Create your models here.

#place is the name i gave to table


class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class People(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()