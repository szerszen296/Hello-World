from functions import *

def main():
    print("Welcome in calculator, enter your arguments:")
    while True:
        x = input("first argument: ")
        print("What calculation would you like to make (+-*/): ")
        calc = input("calculation method: ")
        y = input("second argument: ")
        result = operation(calc, int(x), int(y))
        print(result)
        while True:
            print("What calculation would you like to make (+-*/): ")
            calc = input("calculation method (press enter to finish): ")
            if calc == "":
                exit()
            y = input("second argument (press enter to finish): ")
            if y == "":
                exit()
            result = operation(calc, int(result), int(y))
            print(result)

if __name__ == '__main__':
    main()