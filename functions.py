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
    entry = {}
    if in2 in ["+", "-", "*", "/"]:
        entry = {"first": in1, "operator": in2}
        list.append(entry)
    elif in2 == "=":
        entry = {"second": in1}
        list.append(entry)
    elif in1 in ["+", "-", "*", "/"] and isinstance(in2, (int, float)):
        entry = {"operator": in1, "second": in2}
        list.append(entry)
    elif in1 == "=":
        entry = {"result": in2}
        list.append(entry)
        list.append({"first": in2})
        if do_print:
            print(list)
        return
    elif in1 not in ["+", "-", "*", "/"]:
        if not isinstance(in1, str) or not in1 in ["+", "-", "*", "/", "="]:
            entry = {"result": in1}
            list.append(entry)
            list.append({"first": in1})
            if do_print:
                print(list)
            return
        else:
            return
    else:
        return
    if do_print:
        print(list)

def history(list1):
    print("History:")
    for entry in list1:
        if entry.get("operator") == "=":
            continue
        print(entry)

