from sense_hat import SenseHat
import requests
import time
import json

def GetPrice(Token):
    url  = "https://coingecko.p.rapidapi.com/simple/price"

    querystring = {"ids":Token,"vs_currencies":"usd"}

    headers = {
        'x-rapidapi-key': "XXXX",
        'x-rapidapi-host': "coingecko.p.rapidapi.com"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = json.loads(response.text)
    price = str(result[Token]["usd"])[0:5]
    print (price)
    return (price)

sense = SenseHat()
previousValue = float(0.0)
r = (255,0,0)
g = (0,255,0)
bl = (0,0,255)
w = (255,255,255)
b = (0,0,0)

up_arrow = [b,b,b,b,b,b,b,b,b,b,b,g,g,b,b,b,b,b,g,g,g,g,b,b,b,g,g,g,g,g,g,b,b,b,b,g,g,b,b,b,b,b,b,g,g,b,b,b,b,b,b,g,g,b,b,b,b,b,b,b,b,b,b,b]
down_arrow = [b,b,b,b,b,b,b,b,b,b,b,r,r,b,b,b,b,b,b,r,r,b,b,b,b,b,b,r,r,b,b,b,b,r,r,r,r,r,r,b,b,b,r,r,r,r,b,b,b,b,b,r,r,b,b,b,b,b,b,b,b,b,b,b]
flat_arrow = [b,b,b,b,b,b,b,b,b,b,bl,b,b,bl,b,b,b,bl,bl,b,b,bl,bl,b,bl,bl,bl,bl,bl,bl,bl,bl,bl,bl,bl,bl,bl,bl,bl,bl,b,bl,bl,b,b,bl,bl,b,b,b,bl,b,b,bl,b,b,b,b,b,b,b,b,b,b]


current_marker = 0
max_marker = 64
history = [b] * max_marker

upCount = 0
downCount = 0
neutralCount = 0



while True:

    #On Click Event
    for event in sense.stick.get_events():
        print(event.direction, event.action)

    showValue = float(GetPrice("dogecoin"))

    if (showValue > previousValue):
        sense.set_pixels(up_arrow)
        time.sleep(0.5)
        sense.show_message(str(showValue), text_colour=g)
        upCount += 1
        history[current_marker] = g
    elif (showValue == previousValue):
        sense.set_pixels(flat_arrow)
        time.sleep(0.5)
        sense.show_message(str(showValue), text_colour=bl)
        neutralCount += 1
        history[current_marker] = bl
    else:
        sense.set_pixels(down_arrow)    
        time.sleep(0.5)
        sense.show_message(str(showValue), text_colour=r)
        downCount += 1
        history[current_marker] = r

    # Update the history
    
    current_marker += 1
    if current_marker == max_marker:
        current_marker = 0

    history[current_marker] = w

    sense.set_pixels(history)


    previousValue = showValue


    for i in range(60):
        for event in sense.stick.get_events():
            # Only trigger on release
            if event.action == "pressed":
                sense.show_message(str(showValue), text_colour=w)
                sense.set_pixels(history)
            print(event.direction, event.action)

        time.sleep(1)
        
        