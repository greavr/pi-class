# Step1: Prompt for name
# Step2: Pick a random color
# Step3: show the name on the LED display
#from sense_emu import SenseHat
from sense_hat import SenseHat
import random

sense = SenseHat()

name = input("Enter your name: ")
colour = input("Enter a colour (1 = red, 2 = blue, 3 = green): ")

 
if colour == "1":
    sense.show_message(name, text_colour=(255,0,0))
elif colour == "2":
    sense.show_message(name, text_colour=(0,0,255))
else:
    sense.show_message(name, text_colour=(0,255,0))

