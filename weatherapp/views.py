from urllib import response
from django.shortcuts import render
from decouple import config
import requests
from pprint import pprint
from django.contrib import messages

def home(request):
    API_Key = config('API_KEY')
    u_city = request.GET.get("name")
    if u_city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={u_city}&appid={API_Key}&units=metric"
        response = requests.get(url)
        


    content = response.json()

    


    city = 'Yozgat'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&units=metric"
    response = requests.get(url)
    content = response.json()
    pprint(content)

    context = {

    'city' : content['name'],
    'temp' : content['main']['temp'],
    'icon' : content['weather'][0]['icon'],
    'desc' : content['weather'][0]['description']
    }

    return render(request, 'weatherapp/home.html', context)
