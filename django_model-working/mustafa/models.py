from operator import mod
from django.db import models

class Student(models.Model):
    isim = models.CharField(max_length=50)
    soyisim = models.CharField(max_length=30)
    numara = models.IntegerField()

