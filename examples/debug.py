#hello everyone

def sub(num1,num2):
    return(num1-num1)

def multi(num1,num2):
    return(num1*num2)

def complex(num1,num2):
    # Add two numbers together
    # multiple the combined number by num2
    # sub num1 from the multipled numer
    value = num1 + num2
    print("add value = ", value)
    value = value * num2
    print("multiply value = ", value)
    value -= num1
    print("Minus value= ", value)
    return (value)


print(str(sub(50,50)))


