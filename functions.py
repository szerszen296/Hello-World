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

def get_arg(prompt, *_):
    val = input(prompt).strip()
    if "," in val:
        try:
            return [float(v.strip()) for v in val.split(",")]
        except ValueError:
            print("Invalid list input. Please enter valid numbers separated by commas.")
            return get_arg(prompt)
    else:
        try:
            return float(val)
        except ValueError:
            return 0
           


def print_result(calc, x, y):
    try:
        listx = isinstance(x, list)
        listy = isinstance(y, list)
        if calc == "+" and (listx or listy):
            nums = []
            if listx:
                nums.extend(x)
            elif isinstance(x, (int, float)):
                nums.append(x)
            if listy:
                nums.extend(y)
            elif isinstance(y, (int, float)):
                nums.append(y)
            elif listx and y == "":
                sum(x)
            elif listy and x == "":
                sum(y)
            result = sum(nums)
            
        else:
            if listx or listy:
                print("Only adding is possible for lists.")
                return None
            result = suma(x, y) if calc == "+" else operation(calc, x, y)
        result = round(result, 1)
        print(result)
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return x




