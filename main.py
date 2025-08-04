from functions import *

numbers = []

def main():
    print("Welcome in calculator, enter your arguments (press Enter to finish):")
    while True:
        number = input("argument: ")
        if number == "":
            break
        numbers.append(int(number))

    print("What calculation would you like to make (+-*/): ")
    calc = input("calculation method: ")

    print(operation(calc, *numbers))
if __name__ == '__main__':
    main()