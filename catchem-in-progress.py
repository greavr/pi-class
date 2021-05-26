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

# Def intro function
def intro():
    # Show title
    # Countdown to start
    global catcher_color, score, game_over
    sense.show_message("Dont drop the baby!", text_colour=catcher_color, scroll_speed=0.05)
    
    count_from = 3
    while count_from > 0:
        sense.show_letter(str(count_from))
        time.sleep(1)
        count_from -= 1
        
    game_over = False
    score = 0
    new_berry()
    

# Def move functions
def move_left():
    global catcher_x
    if catcher_x >= 1:
        catcher_x -= 1

def move_right():
    global catcher_x
    if catcher_x < 7:
        catcher_x += 1

# Def new round function
def new_berry():
    global berry_y, berry_x, score, catcher_color
    #Show the current level
    sense.show_message(str(score), scroll_speed=0.055, text_colour=catcher_color)
    
    # Reset the berry Y, and pick a random column (x) for the berry spawn in
    berry_y = 0
    berry_x = random.randrange(0,7)
    
# redraw the screen to show the new position of the berry, the catcher. Handles game over
def update():
    global berry_x, berry_y, game_over, catcher_color, catcher_x, fruit_color, mystery_color
    
    #Clear the display
    sense.clear()
    #Draw our catcher on the bottom row
    sense.set_pixel(catcher_x, 7, catcher_color)
    
    # Drop down the berry and paint berry on the screen
    if berry_y < 7:
        berry_y += 1
        sense.set_pixel(berry_x,berry_y,fruit_color)
    else:
        # Failwhale
        sense.show_message("Game Over!", text_colour=mystery_color, scroll_speed=0.05)
        game_over = True
        sense.show_message("Score: " + str(score))
        time.sleep(1)
        intro()

# intro game
intro()

# Main game loop
while game_over == False:
    # Capture user input
    for event in sense.stick.get_events():
        print(event)
        # Capture if left
        if event.action == "pressed" and event.direction == "left":
            move_left()
        
        if event.action == "pressed" and event.direction == "right":
            move_right()
            
    # Check for collision
    if (catcher_x == berry_x) and (berry_y == 7):
        sense.show_message("You got one!", scroll_speed=0.055)
        score += 1
        # Drop a new berry
        new_berry() 
        
    # Update the display
    update()
    wait_time = 0.5 - (score / 100)
    print(str(wait_time))
    time.sleep(wait_time) # This is difficulty
            
        