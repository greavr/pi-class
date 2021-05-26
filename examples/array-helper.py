# Program to move a cursor from one side of the screen to another
# Step 1: Clear the screen
# Step 2: Read input from the joystick
# Step 3: Update the pixel position on the screen

# Declare Imports
from sense_emu import SenseHat

# Declare variables
sense = SenseHat()
color_past = (255,255,255) #White
color_current = (255,0,0) #red
color_default = (0,0,0) #black

current_location = 0

history = [color_default] * 64

# clear screen
sense.clear()

# Function to move
def MoveMarker(Step):
    global history, current_location, color_past, color_current
    
    # Set current location to our past color
    history[current_x_location] = color_past
    
    # Work out the input provided
    if Step == "left":
        current_location -= 1
    if Step == "right":
        current_location += 1
        
    # Logic check
    if current_location < 0:
        current_location = 63
    elif current_location > 63:
        current_location = 0
        
    history[current_location] = color_current
    

# Main loop
while True:
    # Capture user input
    for event in sense.stick.get_events():
        # Only react to released events
        if event.action == "released":
            MoveMarker(event.direction)
    
    # Lets paint the display
    sense.set_pixels(history)