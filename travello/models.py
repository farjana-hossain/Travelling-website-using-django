from django.db import models

# Create your models here.


class Destination(models.Model):  # inheriting freature of  model
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class Contact(models.Model):  # inheriting freature of  model
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
