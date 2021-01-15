from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from weatherapp.models import City
import json
import requests
from django.conf import settings

selected_range = 3
selected_city = 'Ankara'

@login_required
def dashboard(request):
    global selected_range, selected_city
    cities = City.objects.all()
    city_data = city_data_load()
    return render(request,'dashboard.html',{'cities': cities,'data':city_data, 'selected':selected_city,'range':selected_range})
       

def city_data_load():
    global selected_range, selected_city
    selected_city_obj = City.objects.get(name=selected_city)
    latitude = str(selected_city_obj.latitude)
    longitude = str(selected_city_obj.longitude)
    #key = str(settings.API_SECRET_KEY)
    key = '4a622ad8c7ae45aba3c122145211301'
    url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx?key=' + key + '&q='+latitude+','+longitude+'&format=json&num_of_days='+str(selected_range)
    json_data=requests.get(url).json()['data']
    for data in json_data['weather']:
        for d in data['hourly']:
            d.update((k,v[:-2] + ':' + v[-2:]) for k, v in d.items() if k == "time" and len(v)>2)
    return json_data

def three_days(request):
    global selected_range
    selected_range = 3
    return HttpResponseRedirect(reverse('dashboard'))

def five_days(request):
    global selected_range
    selected_range = 5
    return HttpResponseRedirect(reverse('dashboard'))

def city_change(request):
    global selected_city
    selected_city = request.GET['city']
    return HttpResponse(status=204)