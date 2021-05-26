from sense_emu import SenseHat
sense = SenseHat()
green = (0,255,0)
white = (255,255,255)
sense.show_message("test", text_colour=green,back_colour=(255,255,255))