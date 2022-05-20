
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>Merhaba Dünya</h1>")

def special(request):
    context = {
        'title': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }
    return render(request, 'app/special.html',context)
