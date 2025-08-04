def sum(*numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result += n
    print(result)

def sub(*numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result -= n
    print(result)

def multi(*numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result *= n
    print(result)

def div(*numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result /= n
    print(result)

def operation(calc, *numbers):
    if calc == "+":
        sum(*numbers)
    elif calc == "-":
        sub(*numbers)
    elif calc == "*":
        multi(*numbers)
    elif calc == "/":
        div(*numbers)
    else:
        return("Wrong calculation option. (+-*/)")