from unicodedata import category
from django.contrib import admin

from store.models import Category

# Register your models here.

admin.site.register(Category)