def sum(x, y):
    if type(x) == str:
        print("x should be a number") 
    elif type(y) == str:
        print("y should be a number")
    else:
        print(x + y)

def sub(x, y):
    if type(x) == str:
        print("x should be a number") 
    elif type(y) == str:
        print("y should be a number")
    else:
        print(x - y)

def multi(x, y):
    if type(x) == str:
        print("x should be a number") 
    elif type(y) == str:
        print("y should be a number")
    else:
        print(x * y)

def div(x, y):
    if type(x) == str:
        print("x should be a number") 
    elif type(y) == str:
        print("y should be a number")
    else:
        print(x / y)
    
def operation(calc, x, y):
    if calc == "+":
        sum(x,y)
    elif calc == "-":
        sub(x,y)
    elif calc == "*":
        multi(x,y)
    elif calc == "/":
        div(x,y)
    else:
        return("Wrong calculation option. (+-*/)")