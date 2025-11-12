import requests
import json

choice = True
while choice == True:
    print("Weather Information from OpenWeather API")
    city = input("Please type in your city here:")


    API = '37b67a41a18ae3b7114ed0aeacdb00e6'
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=imperial"

    response = requests.get(URL)
    data = response.json()

    if response.status_code == 200:

        temp = data['main']['temp']
        weather_desc = data ['weather'][0]['description']

        print(f'The temperature in {city} is:', temp, 'Fahrenheit')
        print('Description:', weather_desc)

    else: print(response.status_code)

    choice = input("Do you want to search another city? (yes/no): ")

    if choice == "yes":
        choice = True

else:
    choice = False
    print('Thank you for your time. Goodbye!')