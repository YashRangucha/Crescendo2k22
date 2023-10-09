from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name  = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True)
    desc = models.CharField(max_length=300, null=True)
    
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Regstray(models.Model):
    name = models.CharField(blank=True, max_length=30)
    pname = models.CharField(blank=True, max_length=30)
    img = models.ImageField(null=True, blank=True)
    local = models.EmailField(blank=True, max_length=20)
    desc = models.TextField(blank=True)
    
    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(blank=True, max_length=30)
    date = models.CharField(blank=True, max_length=30)
    email = models.EmailField(max_length=20)
    number = models.IntegerField()
    local = models.CharField(blank=True, max_length=122)
    
    def __str__(self):
        return self.name
