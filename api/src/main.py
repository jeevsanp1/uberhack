import requests
from flask import Flask
import datetime


app = Flask(__name__)

weather_headers = {
    "x-api-key": "22ee2834c449f1b0a5414e42b3096bbd7d51dcde98c28ce00c38450ee987cb89"
}

'''
    - Solar Energy
        - Temperature
        - Cloud Coverage
        
    - Wind Energy
        - Wind Speeds
        
    - HydroElectricity
        - Wind Speeds
        - River Near
        - Change of Temperature
        - Change of Precipitation
        
    - Geothermal
        - ?
'''

def get_weather_urls_by_lat_long(lat, long):
    history = f'https://api.ambeedata.com/weather/history/by-lat-lng?lat={lat}&lng={long}'
    forecast = f'https://api.ambeedata.com/weather/forecast/by-lat-lng?lat={lat}&lng={long}'

    return {
        'history': history,
        'forecast': forecast
    }


@app.route('/')
def home():
    return "Hi"

def forecast_usage(f):
    avg_cloud_coverage = 0
    avg_wind_speed = 0
    avg_temp = 0
    avg_precip_intensity = 0
    tot = len(f)
    for i in f:
        avg_temp += float(i['temperature'])
        avg_cloud_coverage += float(i['cloudCover'])
        avg_wind_speed += float(i['windSpeed'])
        avg_precip_intensity += float(i['precipIntensity'])

    avg_diffs_temp = 0
    avg_diffs_precip = 0

    for i in f:
        avg_diffs_temp = avg_temp - float(i['temperature'])
        avg_diffs_precip = avg_precip_intensity - float(i['precipIntensity'])

    return {
        'cloud': avg_cloud_coverage / tot,
        'wind': avg_wind_speed / tot,
        'temp': avg_temp / tot,
        'temp_change': avg_diffs_temp / tot,
        'precip': avg_precip_intensity / tot,
        'precip_change': avg_diffs_precip / tot
    }


def past_month_stats(base_url):
    dif = 0

    cur_stats = {
        'cloud': 0,
        'wind': 0,
        'temp': 0,
        'temp_change': 0,
        'precip': 0,
        'precip_change': 0
    }

    tot = 3

    for i in range(tot):
        url = base_url + f'&from={str(datetime.datetime.now() - datetime.timedelta(days=(dif+6))).split(".")[0]}&to={str(datetime.datetime.now() - datetime.timedelta(days=dif)).split(".")[0]}'
        new_stats = forecast_usage(requests.get(url, headers=weather_headers).json()['data']['history'])
        cur_stats['cloud'] += new_stats['cloud']
        cur_stats['temp'] += new_stats['temp']
        cur_stats['wind'] += new_stats['wind']
        cur_stats['precip'] += new_stats['precip']
        cur_stats['temp_change'] += new_stats['temp_change']
        cur_stats['precip_change'] += new_stats['precip_change']
        dif += 7

    return {
        'cloud': cur_stats['cloud'] / tot,
        'wind': cur_stats['wind'] / tot,
        'temp': cur_stats['temp'] / tot,
        'precip': cur_stats['precip'] / tot,
        'precip_change': cur_stats['precip_change'] / tot,
        'temp_change': cur_stats['temp_change'] / tot
    }


@app.route('/<lat>/<lng>/<river_near>')
def getter_specific(lat, lng, river_near):
    # geothermal_score = 0
    scores = {
        "solar_energy_score": 0,
        "hydroelectricity_score": 0,
        "wind_energy_score": 0
    }

    history_base_url = get_weather_urls_by_lat_long(lat, lng)['history']
    forecast_url = get_weather_urls_by_lat_long(lat, lng)['forecast']

    forecast = requests.get(forecast_url, headers=weather_headers).json()

    forecast_stats = forecast_usage(forecast['data']['forecast'])

    s = past_month_stats(history_base_url)

    ideal_temperature = 77
    ideal_windspeeds = 13
    ideal_cloudcoverage = 0

    average_scores = {
        'cloud': (forecast_stats['cloud'] + s['cloud']) / 2,
        'wind': (forecast_stats['wind'] + s['wind']) / 2,
        'temp': (forecast_stats['temp'] + s['temp']) / 2,
        'precip': (forecast_stats['precip'] + s['temp']) / 2,
        'precip_change': (forecast_stats['precip_change'] + s['precip_change']) / 2,
        'temp_change': (forecast_stats['temp_change'] + s['temp_change']) / 2
    }

    return "noice"