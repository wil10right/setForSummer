from django.shortcuts import render, redirect, HttpResponse
from .models import *

def setHome(request):
    return render(request, 'setForSummer_app/index.html')

def food(request):
    places = {
        'places': Location.objects.all()
    }
    return render(request, 'setForSummer_app/food.html', places)

def activities(request):
    return render(request, 'setForSummer_app/activities.html')

def learning(request):
    return render(request, 'setForSummer_app/learning.html')

def faqs(request):
    return render(request, 'setForSummer_app/faqs.html')

def contact(request):
    return render(request, 'setForSummer_app/contact.html')

def map_id(request,id):
    map = Location.objects.get(id=id)
    return render(request,'setForSummer_app/map.html',{
        'map_id': map.id,
        'lat':map.lat,
        'lon':map.lon,
    })
