#A pointer is a value that points to the memory address of another variable.
#Pass objects rather than create copies of them. Point to the data rather than make dupes of it. More important in smaller machines and faster
x = 10
print(f"x: {x}")
y = x
print(f"x: {x} -- y: {y}")
x = 11
print(f"x: {x} -- y: {y}")

##id() returns the object’s memory address.
print(f"Memory Address of X: {id(x)}")

x += 1
print(f"x: {x}")
print(f"Memory Address of X: {id(x)}")





