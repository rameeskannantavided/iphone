from django.db import models

# Create your models here.
class Iphone(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.CharField(max_length=50)
    img = models.ImageField(upload_to='gallery')
