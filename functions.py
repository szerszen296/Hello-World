from ast import While


def suma(x, y):
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
    if prompt.isdigit():
        return float(prompt)
    elif prompt == "":
        return None
    else:
        return input(prompt)

def get_arg(prompt, list1, lsit2):
    val = input(prompt)
    if val == "list1":
        return list1
    elif val == "list2" or val == "lsit2":
        return lsit2
    elif val == "":
        return None
    else:
        try:
            return float(val)
        except ValueError:
            print("Invalid input, please enter a number or list name.")
            return get_arg(prompt, list1, lsit2)

def print_result(calc, x, y):
    try:
        if calc == "+" and (isinstance(x, list) or isinstance(y, list)):
            nums = []
            if isinstance(x, list):
                nums.extend(x)
            elif isinstance(x, (int, float)):
                nums.append(x)
            if isinstance(y, list):
                nums.extend(y)
            elif isinstance(y, (int, float)):
                nums.append(y)
            result = sum(nums)
        else:
            if isinstance(x, list) or isinstance(y, list):
                print("Only adding is possible for lists.")
                return None
            result = suma(x, y) if calc == "+" else operation(calc, x, y)
        print(result)
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return x
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return x

