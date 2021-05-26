# class about a car object
# values we can save and edit
# Very basic built in function

class car:
    def __init__(self,make,model,doors=4,color="black"):
        self.make = make
        self.model = model
        self.doors = doors
        self.color = color
        self.engine ="Meaty v8"
        
    def describe(self):
        return (f"You drive a {self.make}, {self.model}, which has {self.doors} doors, and is a nice {self.color} color")


myCar = car(make="ford",model="f150",color="red")
myCar2 = car(make="tesla",model="cybertruck", doors=2,color="silver")

print(myCar.describe())
print(myCar2.doors)
myCar.doors += 1
print(myCar.doors)

class player:
    def __init__(self,x,y,health=1,str=10):
        self.x = x
        self.y = y
        self.health = health
        self.str = str
        
    def get_hurt(damage=1):
        self.health -= damage
        self.x -= damage
    
while true:
    thisPlayer = player(x=0,y=0,health=5)
    if thisPlayer == hurt:
        thisPlayer.get_hurt(damage=2)
        
    sense.draw_pixel(thisPlayer.x,thisPlayer.y,)