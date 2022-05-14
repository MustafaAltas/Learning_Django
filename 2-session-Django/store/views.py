from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hoşgeldin")

# Create your views here.
