import imp
from multiprocessing.spawn import import_main_path
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Merhaba")
