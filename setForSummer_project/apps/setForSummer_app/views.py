from django.shortcuts import render, redirect, HttpResponse
from .models import *

def setHome(request):
    return render(request, 'setForSummer_app/index.html')

def food(request):

    return render(request, 'setForSummer_app/food.html')

def activities(request):
    return render(request, 'setForSummer_app/activites.html')

def map_id(request,id):
    map = Location.objects.get(id=id)
    return render(request,'setForSummer_app/map.html',{
        'lat':map.lat,
        'lon':map.lon,
    })