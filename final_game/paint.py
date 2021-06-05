# Handle imports
import time
from sense_emu import SenseHat
import sys

#Create sense object and clear display
sense = SenseHat()
sense.clear()

# Variables
version ="0.1"
save_loc = "save.file"

# Colours
Title = (245, 139, 17)
MenuText_1 = (0,255,255) #Cyan
MenuText_2 = (0,200,200) #light cyan
MenutText_3 = (237, 50, 56) # light read
colour_list = [(255,255,255),(220,20,60),(255,0,0),(255,127,80),(205,92,92),(240,128,128),(255,160,122),(255,140,0),(255,165,0),(184,134,11),(218,165,32),(238,232,170),(255,255,0),(85,107,47),(107,142,35),(127,255,0),(173,255,47),(50,205,50),(152,251,152),(143,188,143),(46,139,87),(102,205,170),(60,179,113),(32,178,170),(72,209,204),(175,238,238),(127,255,212),(95,158,160),(70,130,180),(100,149,237),(30,144,255),(173,216,230),(0,0,139),(139,0,139),(0,0,205),(65,105,225),(75,0,130),(106,90,205),(123,104,238),(147,112,219),(139,0,139),(153,50,204),(238,130,238),(255,0,255),(218,112,214),(199,21,133),(219,112,147),(255,105,180),(255,192,203),(139,69,19),(210,105,30),(205,133,63),(244,164,96),(210,180,140),(188,143,143),(255,222,173),(176,196,222),(230,230,250),(240,248,255),(240,255,240),(255,255,240),(128,128,128),(211,211,211),(0,0,0)]

# Cursor Position
cursor_x = 0
cursor_y = 0

# Function Set color
def ChangeColor(current_color):
    # Change color by default up in array
    global colour_list
    # Find color in array, error handling
    try:
        current_loc = colour_list.index(current_color)
        current_loc += 1
    except:
        current_loc = 0

    
    # Return location value
    return colour_list[current_loc]

# Pretty intro
def color_scale(duration=1):
    # Paint each pixel a different color
    sense.clear()
    sense.set_pixels(colour_list)
    time.sleep(duration)

# Move Functions
def move(direction):
    global cursor_x, cursor_y
    if direction == "left":
        if cursor_x >= 1:
            cursor_x -= 1
    elif direction == "right":
        if cursor_x < 7:
            cursor_x += 1
    elif direction == "up":
        if cursor_y >= 1:
            cursor_y -= 1
    else:
        if cursor_y < 7:
            cursor_y += 1

# Function to set pixel
def paint_pixel(color):
    global cursor_x, cursor_y
    # Paint current pixel
    sense.set_pixel(cursor_x,cursor_y,color)

# Function to save
def SaveImage():
    # Save current image array
    global save_loc
    # Get pixel list
    pixel_list = sense.get_pixels()

    # Save file
    #try:
    save_file = open(save_loc, "w")
    save_file.write(pixel_list)
    save_file.close()
    #except:
    #    e = sys.exc_info()[0]
    #    print ("Unable to save:")
    #    print (str(e))

# Function to load saved image
def LoadImage():
    # Load saved image from set location
    global save_loc

    # Default value:
    result = [(0,0,0)] * 64

    # Open file, load results
    try:
        result = open(save_loc, "r")
    except:
        e = sys.exc_info()[0]
        print (f"Unable to laod file {save_loc} :")
        print (str(e))

    return (result)

# Function For Menu
def Menu():
    # Function to show options:
    # Show options, use left / right to select options 1/2 then click
    ## 1: New
    ## 2: Load
    ## 3: Show pixel pallet
    global MenuText_1, MenuText_2
    sense.show_message("1: New Image", text_colour=MenuText_1, scroll_speed=0.05)
    sense.show_message("2: Load Image", text_colour=MenuText_2, scroll_speed=0.05)
    sense.show_message("3: Show Pallet", text_colour=MenuText_2, scroll_speed=0.05)

    # Default to new image
    selected_option = 1

    # Wait for input
    while True:
        # Show option
        sense.show_letter(str(selected_option),text_colour=MenuText_2)

        # Check for event
        for event in sense.stick.get_events():
            # If click then do main loop
            if event.action == "pressed" and event.direction == "middle":
                # Check for selected option
                if selected_option == 2:
                    # Load Image
                    MainLoop(LoadImage())
                elif selected_option == 3:
                    # Show colors
                    color_scale(5)
                else:
                    # New image
                    MainLoop()
            
            # Now change option
            if event.action == "pressed" and (event.direction == "left"):
                if selected_option >= 1:
                    selected_option -= 1
            if event.action == "pressed" and (event.direction == "right"):
                if selected_option < 3:
                    selected_option += 1

# Function For Into
def intro():
    # Show welcome message & version
    global version, Title, MenuText_2, MenutText_3
    sense.show_message("Paint", text_colour=Title, scroll_speed=0.04)
    sense.show_message("V: " +version,text_colour=MenutText_3, scroll_speed=0.05)
    color_scale()

    # Call main menu
    Menu()

# Main Game Loop
def MainLoop(ImageCanvas=[]):
    global cursor_x, cursor_y

    # Clear Image
    # If Loaing image do that
    # Else Start new image

    # Basic controls
    ## Click to change color
    ## Shake to undo last pixel
    ## Paint as you go

    # Clear Display
    sense.clear()

    # If Image Set load image
    if ImageCanvas:
        sense.set_pixels(ImageCanvas)

    # Set cursor position
    cursor_color = (255,255,255) # white default

    # Main loop
    while True:
        # Paint the cursor
        sense.set_pixel(cursor_x,cursor_y,cursor_color)

        # Do move event
        for event in sense.stick.get_events():
            # Capture if left
            if event.action == "pressed" and event.direction != "middle":
                move(event.direction)
            
            elif event.action == "pressed" and event.direction == "middle":
                cursor_color = ChangeColor(cursor_color)

            elif event.action == "held" and event.direction == "middle":
                # Save and quit
                SaveImage()
                Menu()
        
    



# Code to run
## Show Intro
intro()