import geocoder
import requests
from secrets import API_KEY

destinations = [
    'Space Needle',
    'Crater Lake',
    'Golden Gate Bridge',
    'Yosemite National Park',
    'Las Vegas, Nevada',
    'Grand Canyon National Park',
    'Aspen, Colorado',
    'Mount Rushmore',
    'Yellowstone National Park',
    'Sandpoint, Idaho',
    'Banff National Park',
    'Capilano Suspension Bridge',
]

API_BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# result = geocoder.arcgis(destinations[0]).latlng
# print(result)

for destination in destinations:
    lat, lng = geocoder.arcgis(destination).latlng
    print(f'{destination} is located at ({lat}, {lng})')
    full_api_url = f'{API_BASE_URL}?lat={lat}&lon={lng}&appid={API_KEY}'
    result = requests.request('GET', full_api_url).json()
    weather_description = result['weather'][0]['description']
    temperature = result['main']['temp']
    converted_temp = (temperature - 273.15) * (9/5) + 32
    float_temp = int(converted_temp)
    print(f"At the {destination} right now, there are {weather_description} with a temperature of {float_temp}")