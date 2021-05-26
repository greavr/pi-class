# Dont Eat My Brains
# Avoid the incoming zombies
# Objects: Player, Zombie, Wall, Hole
# Game loop:
# Player moves in 4d,
# zombies always walk towards player.
# Only way to remove zombies is to drop them into holes.
# Player can not fall into hole
# Player have 3 health
import random
import time

from sense_hat import SenseHat
sense = SenseHat()

# Colours
wall_colour = (255,255,0)
hole_colour = (255,0,0)
background_colour = (25,25,25)

# Player class
class Player:
    # Default to 3 health, and start in the middle
    def __init__(self, x=4, y=4, color=(0, 0, 255), health=3):
        self.x = x
        self.y = y
        self.color = color
        self.health = health
        self.alive = True
        
    def take_damage(self):
        # Reduce health by 1 and change color
        self.health -= 1
        if self.health == 2:
            self.color = (51, 52, 195)
        elif self.health == 1:
            self.color = (57, 58, 152)
        elif self.health == 0:
            self.alive = False
            
    def move(self, direction):
        # move in direction
        if direction == "left":
            if self.x >= 1:
                self.x -= 1
        elif direction == "right":
            if self.x < 7:
                self.x += 1
        elif direction == "up":
            if self.y >= 1:
                self.y -= 1
        else:
            if self.y < 7:
                self.y += 1
# Zombie class
class Zombie:
    def __init__(self, x, y, init=0, speed=5):
        self.x = x
        self.y = y
        self.speed = speed
        self.init = init
        self.color = (51, 255, 51)
    
    def move(self, target_player, wall_list):
        #Pass a player object to head toward player x,y
        move_options = self.check_area(walls=wall_list, target=target_player)

        moved = False
        # move x
        if target_player.x > self.x and bool(move_options["right"]):
            self.x += 1
            moved = True
        elif target_player.x < self.x and bool(move_options["left"]):
            self.x -= 1
            moved = True
        elif target_player.x == self.x:
            pass
        
        # move y
        if not moved:
            if target_player.y > self.y and bool(move_options["up"]):
                self.y += 1
            elif target_player.y < self.y and bool(move_options["down"]):
                self.y -=1
            elif target_player.y == self.y:
                pass

    def check_death(self, holes):
        # Check if on a death spot
        result = False
        for aHole in holes:
            if (self.x == aHole[0]) & (self.y == aHole[1]):
                # Zombie in a hole
                result = True

        # Return result
        return result
    # Check Collisions
    def check_area(self, walls, target):
        # Function to return outcome
        # Return array of outcomes
        # Itterate over walls
        result = {"right" : False, "left" : False, "down": False, "up": False}

        # Itterate over walls
        for aWall in walls:
            if ((self.x +1)== aWall[0]) or (self.x == 7):
                result["right"] = True
            elif ((self.x -1)==aWall[0]) or (self.x == 0):
                result["left"] = True
            elif ((self.y +1)==aWall[1]) or (self.y == 7):
                result["down"] = True
            elif ((self.y -1)==aWall[1]) or (self.y == 0):
                result["up"] = True
        
        # Check for bite
        chomp = False
        if (((self.x +1) == target.x) or ((self.x -1)== target.x)) and (((self.y +1)== target.y) or ((self.y -1)==target.y)):
            chomp = True
        
        # Do damage
        if chomp:
            target.take_damage()

        return result

# Create Maps
def get_map(id=1):
    # Return pre-defined map
    walls = []
    holes = []
    result = dict()

    # Map 1
    if id == 1:
        walls = [[1,1],[1,2],[1,3],[3,1],[3,2],[3,3],[1,5],[1,6],[2,6],[3,6],[6,1],[6,2],[6,3],[6,4],[6,6]]
        holes = [[2,2],[5,4]]
        zombies = [[0,0,5],[7,7,5]]
    elif id == 2:
        walls = [[1,2],[1,3],[1,4],[1,5],[1,6],[6,6],[6,5],[6,4],[6,3],[6,1],[4,5],[4,6],[5,6],[6,6],[4,3],[4,4],[5,4]]
        holes = [[0,4],[7,3]]
        zombies = [[0,0,5],[7,7,5],[0,7,5],[7,0,5]]
    else:
        walls = [[1,1],[1,2],[1,3],[3,1],[3,2],[3,3],[1,5],[1,6],[2,6],[3,6],[6,1],[6,2],[6,3],[6,4],[6,6]]
        holes = [[5,4]]
        zombies = [[0,0,3],[7,7,5],[0,7,5],[7,0,6]]
    
    result['walls'] = walls
    result['zombies'] = zombies
    result['holes'] = holes

    return result

# Start A New Game
def new_game(level=1):
    # Function For New Game
    aPlayer = Player()
    zombie_list = []

    # Get the map
    map = get_map(level)

    # Spawn the zombies
    for aZombie in map['zombies']:
        new_zombie = Zombie(x=aZombie[0],y=aZombie[1],speed=aZombie[2])
        zombie_list.append(new_zombie)

    # Main Game Loop
    game_running = True
    while game_running:
        # Game logic
        
        # Paint the display Background color
        sense.clear()
        sense.set_pixels([background_colour] * 64)

        # Draw Player
        sense.set_pixel(aPlayer.x, aPlayer.y, aPlayer.color)

        # Draw Walls & Holes
        for aWall in map['walls']:
            sense.set_pixel(aWall[0],aWall[1],wall_colour)
        for aHole in map['holes']:
            sense.set_pixel(aHole[0],aHole[1],hole_colour)

        # Draw Zombies
        for aZombie in zombie_list:
            # Stall the zombies, move every other cycle
            if  aZombie.init == aZombie.speed:
                # Check moves
                aZombie.move(target_player=aPlayer, wall_list=map['walls'])
                aZombie.init = 0
            else:
                aZombie.init += 1

            # Always draw the zombies
            if not aZombie.check_death(map['holes']):
                sense.set_pixel(aZombie.x, aZombie.y, aZombie.color)
            else:
                # Kill zombie
                zombie_list.remove(aZombie)
        
        # Capture input
        for event in sense.stick.get_events():
            if event.action == "pressed" and event.direction != "middle":
                aPlayer.move(event.direction)
        
        # Wait
        time.sleep(0.5)

        # Check end round conditions
        if not aPlayer.alive:
            # Player died
            game_running = False
        elif len(zombie_list) == 0:
            # Last Zombie Dead
            game_running = False
    
    # Post Game Loop
    return (aPlayer.alive)
    
# Main loop
current_level = 1
outcome = new_game(level=current_level)
if outcome:
    print("Winner")
else:
    print("Died")