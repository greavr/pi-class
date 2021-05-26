# Handle imports
from sense_emu import SenseHat
import time
import random

#Create sense object and clear display
sense = SenseHat()
sense.clear()

# Randomly pick a X position for the fruit
# Move the fruit down the Y axis
# Capture user input to move the basket on the X axis

# Variables
game_over = False
catcher_x = 4
score = 0
berry_x = random.randrange(0,7)
berry_y = 0

# Colors
catcher_color = (0,255,255) # cyan
fruit_color = (255,0,128) #dark pink
mystery_color = (255,128,0) # Orange

# Def move functions
def move_left():
    global catcher_x
    if catcher_x >= 1:
        catcher_x -= 1

def move_right():
    global catcher_x
    if catcher_x < 7:
        catcher_x += 1

# Def Into
def intro():
    global game_over, catcher_color, score
    # Show intro
    sense.show_message("Catchem!", text_colour=mystery_color, scroll_speed=0.05)

    #Loop count down
    i = 3
    while i > 0:
        sense.show_letter(str(i))
        time.sleep(1)
        i -= 1

    sense.set_pixel(0, 7 , catcher_color)

    # Start the game
    game_over = False
    score = 0
    new_berry()

# Def New game function
def new_berry():
    global berry_y, berry_x, score
    sense.show_message( str(score), scroll_speed=0.055, text_colour=catcher_color)

    berry_y = 0
    berry_x = random.randrange(0,7)

# Define move berry function
def update():
    global berry_x, berry_y, game_over, catcher_color, catcher_x
    sense.clear()
    sense.set_pixel(catcher_x, 7, catcher_color)

    # Drop the berty down a row, game over
    if berry_y < 7:
        berry_y = berry_y + 1
        sense.set_pixel(berry_x, berry_y, fruit_color)
    else:
        sense.show_message("Game Over!", text_colour=mystery_color, scroll_speed=0.05)
        game_over = True
        sense.show_message("Score: " + str(score))
        time.sleep(1)
        intro()



# Show intro
intro()

# Main game loop
while game_over == False:
    # Capture user input
    for event in sense.stick.get_events():
        # Capture if left
        if event.action == "pressed" and event.direction == "left":
            move_left()
        
        if event.action == "pressed" and event.direction == "right":
            move_right()

    
    # Check for collision
    if (catcher_x == berry_x) and (berry_y == 7):
            print("You got one!")
            score += 1
            new_berry()

    update()
    # Wait time:
    wait_time = 0.5 - (score / 100)
    print(str(wait_time))
    time.sleep(wait_time)