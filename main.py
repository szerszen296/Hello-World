from functions import *

def main():
    print("Welcome in calculator, enter your arguments:")
    while True:
        x = int(input("first argument: "))
        print("What calculation would you like to make (+-*/): ")
        calc = input("calculation method: ")

        if calc != "+" and calc != "-" and calc != "*" and calc != "/":
            while True:
                print("Wrong calculation option. Please enter one of (+-*/).")
                calc = input("calculation method: ")
                if calc == "+" or calc == "-" or calc == "*" or calc == "/":
                    break

        y = int(input("second argument: "))
        result = operation(calc, int(x), int(y))
        print(result)

        while True:
            print("What calculation would you like to make (+-*/): ")
            calc = input("calculation method (press enter to finish): ")
            if calc == "":
                exit()
            elif calc != "+" and calc != "-" and calc != "*" and calc != "/":
                while True:
                    print("Wrong calculation option. Please enter one of (+-*/).")
                    calc = input("calculation method: ")
                    if calc == "+" or calc == "-" or calc == "*" or calc == "/":
                        break
                    elif calc == "":
                        exit()
                        
            y = int(input("second argument (press enter to finish): "))

            if y == "":
                exit()
            result = operation(calc, int(result), int(y))
            print(result)

if __name__ == '__main__':
    main()