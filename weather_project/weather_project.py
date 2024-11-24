# weather checking app 

import requests

API_KEY = 'e7fc778a8b3eb7a8d01d8192bb78a635'  # Make sure this is a valid API key
city_name = input('Enter the name of the city: ')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'

response = requests.get(url)
print(response)

if response.status_code == 200:
    weather_data=response.json()
    weather_disc=weather_data['weather'][0]['description']
    temp=weather_data['main']['temp']-273.15
    print(f'weatherin{city_name}: {round(temp,2)}  °C with {weather_disc}')



    