from sense_emu import SenseHat

sense = SenseHat()

def showHello():
    sense.clear()
    sense.show_message("Hello world")
    
def showGoodbye():
    sense.clear()
    sense.show_message("Goodbye")

def showQuestion():
    sense.clear()
    sense.show_letter("?")
    
def showText(TextToShow,Colour):
    sense.clear()
    sense.low_light = True
    sense.show_message(TextToShow,text_colour=Colour)

showText("It was the best of times, it was the worst of times",(255,0,0))
showText("What is black and white and red all over? A penguin with a sun tan",(0,255,0))