def sum(x, y):
    if type(x) == str:
        return "x should be a number"
    elif type(y) == str:
        return "y should be a number"
    else:
        return x + y

def sub(x, y):
    if type(x) == str:
        return "x should be a number"
    elif type(y) == str:
        return "y should be a number"
    else:
        return x - y

def multi(x, y):
    if type(x) == str:
        return "x should be a number"
    elif type(y) == str:
        return "y should be a number"
    else:
        return x * y

def div(x, y):
    if type(x) == str:
        return "x should be a number"
    elif type(y) == str:
        return "y should be a number"
    else:
        return x / y

def operation(calc, x, y):
    if calc == "+":
        return sum(x, y)
    elif calc == "-":
        return sub(x, y)
    elif calc == "*":
        return multi(x, y)
    elif calc == "/":
        return div(x, y)
    else:
        return "Wrong calculation option. (+-*/)"
    
def calcoprators(calc):
    while calc not in ["+", "-", "*", "/"]:
        print("Wrong calculation option. Please enter one of (+-*/).")
        calc = input("calculation method: ")
        if calc == "":
            exit()
    return calc

def result_handler(calc, x, y):
    try:
        result = operation(calc, float(x), float(y))
        return(result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

def get_calc():
    print("What calculation would you like to make (+-*/): ")
    calc = input("calculation method: ")
    return calcoprators(calc)

def get_number(prompt):
    return float(input(prompt))

def print_result(calc, x, y):
    try:
        result = operation(calc, x, y)
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return x 
    
def append_calculation(in1, in2, list, do_print):
    if in1 != "":
        list.append(in1)
    if in2 != "":
        list.append(in2)
    if do_print == True:
        print(list)

