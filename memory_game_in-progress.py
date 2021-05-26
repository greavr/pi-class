from sense_emu import SenseHat
import time
import random

sense = SenseHat()

#declare color tuples
r = (10,0,0)
w = (255,255,255)
k = (0,0,0)


no_arrow = [
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

left_arrow =[   
w,w,w,w,w,w,w,w,
w,w,r,w,w,w,w,w,
w,r,r,w,w,w,w,w,
r,r,r,r,r,r,r,w,
w,r,r,w,w,w,w,w,
w,w,r,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

right_arrow =[   
w,w,w,w,w,w,w,w,
w,w,w,w,w,r,w,w,
w,w,w,w,w,r,r,w,
w,r,r,r,r,r,r,r,
w,w,w,w,w,r,r,w,
w,w,w,w,w,r,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w
]

down_arrow =[   
w,w,w,w,w,w,w,w,
w,w,w,r,w,w,w,w,
w,w,w,r,w,w,w,w,
w,w,w,r,w,w,w,w,
w,w,w,r,w,w,w,w,
w,r,r,r,r,r,w,w,
w,w,r,r,r,w,w,w,
w,w,w,r,w,w,w,w
]

up_arrow =[   
w,w,w,r,w,w,w,w,
w,w,r,r,r,w,w,w,
w,r,r,r,r,r,w,w,
w,w,w,r,w,w,w,w,
w,w,w,r,w,w,w,w,
w,w,w,r,w,w,w,w,
w,w,w,r,w,w,w,w,
w,w,w,r,w,w,w,w
]
 
#list of arrows
arrows = ["up", "right", "down", "left"]


#variable to hold level
level = 0

current_pattern = []
player_pattern = []
player_turn = False #Boolean is either true or false

def submit_guess():
    # Compare the player guess's with the computer random choice to see if player was right
    global player_pattern, current_pattern, player_turn,r ,w, level
    
    if current_pattern == player_pattern:
        # yay the player was right
        sense.show_message("LEVEL CLEAR", text_colour=r, back_colour=w, scroll_speed=2)
        player_turn = False
    else:
        sense.show_message("Game Over", text_colour=w, back_colour=r, scroll_speed=3)
        level = 0
        player_turn = False
    
def next_level():
    # Increase the difficulty
    # Create a new random pattern
    # Set player turn to true
    global player_pattern, current_pattern, level, player_turn, arrows
    
    level += 1
    # Show the current level
    sense.show_message("Level: " + str(level))
    
    # Reset the patterns
    player_pattern = []
    current_pattern = []
    
    # Create the random list of directions to show, where the # of directions is the level
    for i in range(level):
        current_pattern.append(random.choice(arrows))
        
    # Display the pattern
    for arrow in current_pattern:
        if arrow == "up":
            sense.set_pixels(up_arrow)
        elif arrow == "right":
            sense.set_pixels(right_arrow)
        elif arrow == "left":
            sense.set_pixels(left_arrow)
        else:
            sense.set_pixels(down_arrow)
            
        # Sleep to let character show
        time.sleep(1)
        sense.set_pixels(no_arrow)
        time.sleep(0.5)
    
    # Outside the for loop
    player_turn = True
            

while True:
    #Step1: Pick a random direction arrow
    if player_turn:
        sense.show_letter("?")
        #Step2: Capture user input
        # Code to capture and filter user input
        for event in sense.stick.get_events():
            # Only capture the pressed event, not released
            # Any direction but middle
            if event.action == "pressed" and event.direction != "middle":
                player_pattern.append(event.direction)
            
            # Capture submit
            if event.action == "released" and event.direction == "middle":
                print("player: " + str(player_pattern))
                submit_guess()
                

    else:
        next_level()
        
