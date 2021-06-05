import requests
import json
import time

def get_weather(zip="95008"):
    xx = "c42ab7f32c5d7e2074e7582ae438edeb"
    url = "https://api.openweathermap.org/data/2.5/weather" # Website we want to open

    params = {"zip": zip, "appid": xx, "units" : "imperial"}
    response = requests.request("GET", url, params=params)
    result = json.loads(response.text)

    temperature = result["main"]["temp"] 
    print(temperature)
    return(temperature)


while True:
    current_temperature = get_weather()
    if (current_temperature >= 70) and (current_temperature <= 65):
        # Sunny
        print("sunny")
    elif current_temperature <=50:
        # cold
        print("cold")
    else:
        # regular
        print("meh")

    print(current_temperature)

    time.sleep(60) # Delay before whole process resets