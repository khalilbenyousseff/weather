# views.py
from django.shortcuts import render
from .models import ForecastDay
import requests


def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        # Remplacez par votre véritable clé d'API WeatherAPI
        api_key = '2cd2985ec6da4317984183349230406'
        url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=3&aqi=no'
        forecast_data = requests.get(url).json()
        if 'error' in forecast_data:
            forecast = None
        else:
            city = forecast_data['location']['name']
            forecast = []
            for day in forecast_data['forecast']['forecastday']:
                date = day['date']
                max_temp = day['day']['maxtemp_c']
                min_temp = day['day']['mintemp_c']
                condition = day['day']['condition']['text']
                icon = day['day']['condition']['icon']
                forecast_day = ForecastDay(
                    date, max_temp, min_temp, condition, f'http:{icon}')
                forecast.append(forecast_day)
    else:
        city = 'Paris'
        forecast = None

    return render(request, 'weather/index.html', {'city': city, 'forecast': forecast, 'city': city})
