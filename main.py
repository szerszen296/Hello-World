from functions import *


def main():
    print("Welcome in calculator, enter your arguments:")
    x = input("first argument: ")
    y = input("second argument: ")
    print("What calculation would you like to make (+-*/): ")
    calc = input("calculation method: ")

    print(operation(calc, int(x), int(y)))
if __name__ == '__main__':
    main()