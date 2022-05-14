from django.urls import path
from .views import home,mustafa

urlpatterns = [
    path('', home, name="home"),
    path('mustafa', mustafa, name="mustafa"),
]
