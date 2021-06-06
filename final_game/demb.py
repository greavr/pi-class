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

# Parent Generic Class
class Generic:
    def __init__(self,x=0,y=0,color=(0,0,0)):
        self.x = x
        self.y = y
        self.color = color
        self.alive = True
    
    def move(self, direction, map):
        # move in direction
        moved = False
        
        if (direction == "left") and (self.check_move(walls=map["walls"],direction="left")):
            if self.x >= 1:
                self.x -= 1
            moved = True
        elif (direction == "right") and (self.check_move(walls=map["walls"],direction="right")):
            if self.x < 7:
                self.x += 1
            moved = True
        elif (direction == "down") and (self.check_move(walls=map["walls"],direction="down")):
            if self.y < 7:
                self.y += 1
            moved = True
        elif (direction == "up") and (self.check_move(walls=map["walls"],direction="up")):
            if self.y >= 1:
                self.y -= 1
            moved = True

        return moved


    def check_move(self, walls, direction):
        # validate move direction
        result = True

        # Itterate over walls
        for aWall in walls:
            if ((self.x +1) == aWall[0]) and ((self.y)== aWall[1]) and (direction == "right"):
                print(f"Denied Direction: {direction} -- x,y: {self.x +1},{self.y}, wall x,y: {aWall[0]},{aWall[1]}")
                result = False
                break
            elif ((self.x -1) ==aWall[0]) and ((self.y)== aWall[1]) and (direction == "left"):
                print(f"Denied Direction: {direction} -- x,y: {self.x -1},{self.y}, wall x,y: {aWall[0]},{aWall[1]}")
                result = False
                break
            elif ((self.x) == aWall[0]) and ((self.y +1)==aWall[1]) and (direction == "up"):
                print(f"Denied Direction: {direction} -- x,y: {self.x},{self.y +1}, wall x,y: {aWall[0]},{aWall[1]}")
                result = False
                break
            elif ((self.x) == aWall[0]) and ((self.y -1)==aWall[1]) and (direction == "down"):
                print(f"Denied Direction: {direction}x,y: {self.x},{self.y -1}, wall x,y: {aWall[0]},{aWall[1]}")
                result = False
                break
        
        return result

# Player class
class Player(Generic):
    # Default to 3 health, and start in the middle
    def __init__(self, x=4, y=4, color=(0, 0, 255)):
        super().__init__(x=x,y=y,color=color)
        self.health = 3
    
    def take_damage(self):
        # Reduce health by 1 and change color
        self.health -= 1
        if self.health == 2:
            self.color = (51, 52, 195)
        elif self.health == 1:
            self.color = (57, 58, 152)
        elif self.health == 0:
            self.alive = False
        
# Zombie class
class Zombie(Generic):
    def __init__(self, x, y, init=0, speed=5, color=(51, 255, 51)):
        super().__init__(x=x,y=y,color=color)
        self.speed = speed
        self.init = init
        safe_move = ""
    
    def should_move(self):
        if  self.init == self.speed:
                # Check moves
            self.init = 0
            return True
        else:
            self.init += 1
            return False

    def zombie_move(self, target_player, map):
        # Check Init then move if right
        if not self.should_move():
            # Dont make a move
            return
        
        # Make decision on move
        moved = False
        count = 0
        while not moved:
            if target_player.x > self.x:
                if self.move(map=map,direction= "right"):
                    moved = True
                    self.safe_move = "left"
            elif target_player.x < self.y:
                if self.move(map=map,direction= "left"):
                    moved = True
                    self.safe_move = "right"
            elif target_player.y > self.y:
                if self.move(map=map, direction = "down"):
                    moved = True
                    self.safe_move = "up"
            elif target_player.y < self.y:
                if self.move(map=map, direction= "up"):
                    moved = True
                    self.safe_move = "down"

            
            #only try four moves before stepping back
            if count == 3:
                self.move(map=map, direction=self.safe_move)
                moved = True
            else:
                count += 1


    def check_death(self, holes):
        # Check if on a death spot
        result = False
        for aHole in holes:
            if (self.x == aHole[0]) & (self.y == aHole[1]):
                # Zombie in a hole
                self.alive = False

        # Return result
        return result

    def i_can_chomp(self,player):
        # Check to see if chomp
        # Check for bite
        # Return True / False for screen flash
        chomp = False
        if (((self.x +1) == player.x) or ((self.x -1)== player.x)) and (((self.y +1)== player.y) or ((self.y -1)==player.y)):
            chomp = True
        
        # Do damage
        if chomp:
            player.take_damage()

        # Return outcome
        return chomp

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

# Helper Functions
def draw_map(map):
    # Paint the display Background color
    sense.clear()
    sense.set_pixels([background_colour] * 64)

    # Draw Walls & Holes
    for aWall in map['walls']:
        sense.set_pixel(aWall[0],aWall[1],wall_colour)
    for aHole in map['holes']:
        sense.set_pixel(aHole[0],aHole[1],hole_colour)

def draw_player(character):
    # Draw the location of the character
    sense.set_pixel(character.x, character.y, character.color)

def check_game_condition(player,zombies):
    # Return True for keep playing, false for stop
    result = True
    if not player.alive:
        # Player died
        result = False
    elif len(zombies) == 0:
        # Last Zombie Dead
        result = False
    return result
    
def spawn_zombies(map):
    # Spawn the zombies
    result = []
    for aZombie in map['zombies']:
        new_zombie = Zombie(x=aZombie[0],y=aZombie[1],speed=aZombie[2])
        result.append(new_zombie)
    return result

def chomp():
    # Player Chomped Flash Red
    sense.set_pixels((255,0,0) * 64)
    time.sleep(0.2)

# Primary Game Loop
def game_loop(map,player):
    zombie_list = spawn_zombies(map=map)
    # Main Game Loop
    game_running = True
    while game_running:
        # Draw map
        draw_map(map=map)
        # Draw Player
        draw_player(character=player)
        # Move, draw, chomp zombies
        player_chomped = False
        for aZombie in zombie_list:
            # Move
            aZombie.zombie_move(target_player=player,map=map)
            # Draw pizel
            draw_player(character=aZombie)
            # Check chomp
            if aZombie.i_can_chomp(player=player):
                player_chomped = True
        
        # Capture input
        for event in sense.stick.get_events():
            if event.action == "pressed" and event.direction != "middle":
                player.move(map=map,direction=event.direction)
        
        # Wait
        time.sleep(0.5)

        # Flash the screen if chomped
        if player_chomped:
            chomp()

        # Check end round conditions
        game_running = check_game_condition(player=player,zombies=zombie_list)

    # Post Game Loop
    return (player.alive)

# Game Controller
def game_controller():
    # Function For New Game
    aPlayer = Player()
    current_level = 1
    outcome = True

    # Run game
    while outcome:
        map = get_map(id=current_level)
        outcome = game_loop(map=map, player=aPlayer)
        if outcome:
            print("Winner")
            current_level += 1
        else:
            print("Died")

game_controller()


    
    

    
