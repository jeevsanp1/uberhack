import math

import requests
from flask import Flask
import datetime
from src.helper import solar_price, hydro_price, wind_price

app = Flask(__name__)

weather_headers = {
    "x-api-key": "22ee2834c449f1b0a5414e42b3096bbd7d51dcde98c28ce00c38450ee987cb89"
}

'''
    - Solar Energy (Done)
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
        avg_diffs_temp += (avg_temp / tot) - float(i['temperature'])
        avg_diffs_precip += (avg_precip_intensity / tot) - float(i['precipIntensity'])

    return {
        'cloud': avg_cloud_coverage / tot,
        'wind': avg_wind_speed / tot,
        'temp': avg_temp / tot,
        'temp_change': avg_diffs_temp / tot,
        'precip': abs(avg_precip_intensity / tot),
        'precip_change': abs(avg_diffs_precip / tot)
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

    tot = 2

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


def return_scores(average_scores):
    ideal_temperature = 77
    ideal_windspeeds = 13
    ideal_cloudcoverage = 0

    ideal_precip_change = 0.125
    ideal_temp_change = 0.125

    solar_score = 0
    wind_score = 0
    hydro_score = 0

    temp_dif = ideal_temperature - average_scores['temp']
    if temp_dif < 0:
        solar_score -= temp_dif * 5
    else:
        solar_score += temp_dif * 10

    cloud_dif = ideal_cloudcoverage - average_scores['cloud']
    solar_score -= cloud_dif * 100

    wind_dif = ideal_windspeeds - average_scores['wind']
    if wind_dif < 0:
        wind_score -= wind_dif * 5
    else:
        wind_score += wind_dif * 10

    if average_scores['river']:
        hydro_score += 75

    precip_change_dif = average_scores['precip_change'] - ideal_precip_change
    temp_change_dif = average_scores['temp_change'] - ideal_temp_change

    if temp_change_dif > 0:
        hydro_score += temp_change_dif * 10
    else:
        hydro_score -= temp_change_dif * 5

    if precip_change_dif > 0:
        hydro_score += precip_change_dif * 10
    else:
        hydro_score -= precip_change_dif * 5

    return {
        'wind': wind_score,
        'solar': solar_score,
        'hydro': hydro_score,
    }


def get_pricing(state):
    state_names = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado",
                   "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii",
                   "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts",
                   "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina",
                   "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York",
                   "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina",
                   "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington",
                   "Wisconsin", "West Virginia", "Wyoming"]

    requests.get('https://www.google.com/search?q=average+price+of+solar+panel+in+florida')

    hydro_cost = None
    solar_cost = None
    wind_cost = None

    for s in state_names:
        if s.upper() == state.upper():
            hydro_cost = hydro_price(state)
            solar_cost = solar_price(state)
            wind_cost = wind_price(state)

    return {
        'wind': wind_cost,
        'solar': solar_cost,
        'hydro': hydro_cost
    }


@app.route('/<lat>/<lng>/<river_near>/<max_budget>/<state>')
def getter_specific(lat, lng, river_near, max_budget, state):

    history_base_url = get_weather_urls_by_lat_long(lat, lng)['history']
    forecast_url = get_weather_urls_by_lat_long(lat, lng)['forecast']

    forecast = requests.get(forecast_url, headers=weather_headers).json()

    forecast_stats = forecast_usage(forecast['data']['forecast'])

    s = past_month_stats(history_base_url)

    print(forecast_stats)
    print(s)

    river = False

    if river_near.upper() == "TRUE":
        river = True
    else:
        river = False

    average_scores = {
        'cloud': (forecast_stats['cloud'] + s['cloud']) / 2,
        'wind': (forecast_stats['wind'] + s['wind']) / 2,
        'temp': (forecast_stats['temp'] + s['temp']) / 2,
        'precip': (forecast_stats['precip'] + s['temp']) / 2,
        'precip_change': (forecast_stats['precip_change'] + s['precip_change']) / 2,
        'temp_change': (forecast_stats['temp_change'] + s['temp_change']) / 2,
        'river': river
    }

    print(average_scores)

    prices = get_pricing(state)

    scores = return_scores(average_scores)

    max_budget = float(max_budget)

    for key in prices:
        if prices[key] <= max_budget:
            scores[key] += 50

    return scores
