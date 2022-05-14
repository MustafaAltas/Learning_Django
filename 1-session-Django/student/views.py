from django.shortcuts import render
from django.http import HttpResponse
# Create your tests here.

def home(request):
    return HttpResponse("Mustafa")

def mustafa(request):
    return HttpResponse("Altaş")