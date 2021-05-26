# Program to move a cursor from one side of the screen to another
# Step 1: Clear the screen
# Step 2: Read input from the joystick
# Step 3: Update the pixel position on the screen

# Declare Imports
from sense_hat import SenseHat

# Declare variables
sense = SenseHat()

# Setup our colours
color_past = (255,255,255)
color_current = (255,0,0)
color_default = (0,0,0)

# Used to mark where we are
current_x_location = 0
max_marker = 64

# Create a large array with all the same value
history = [color_default] * max_marker 

# Function to move
def MoveMarker(Step):
    global history, current_x_location

    # This function takes two inputs: move right or left, and current_x_location

    # Set the current position color to our past color
    history[current_x_location] = color_past

    # Lets work out the input
    if Step == "left":
        # Set current_x_location to match the new location & change the color
        current_x_location -= 1
    elif Step == "right":
        # Set current_x_location to match the new location & change the color
        current_x_location += 1

    # Logic check the array boundary
    if current_x_location < 0:
        current_x_location = max_marker-1
    elif current_x_location > max_marker-1:
        current_x_location = 0

    # Update the current location
    history[current_x_location] = color_current
    
    

# Main Loop
while True:
    
        # First lets paint the display
        sense.set_pixels(history)

        # Now lets get user input and tie it to event
        for event in sense.stick.get_events():
            # Only react to released events
            if event.action == "released":
                MoveMarker(event.direction)
        
        # Loop back

