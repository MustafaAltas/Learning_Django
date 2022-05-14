from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
# Create your models here.


#python manage.py makemigrations ile table oluşturulır
#python manage.py migrate database'e sign işlemi
#python manage.py createsuperuser admin girişi için önce register işlemi yapılıyor.
