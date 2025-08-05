from functions import *

def main():
    print("Welcome in calculator, enter your arguments:")
    try:
        while True:
            x = get_number("first argument: ")
            calc = get_calc()
            y = get_number("second argument: ")
            result = print_result(calc, x, y)

            while True:
                calc = input("calculation method (press enter to finish): ")
                if calc == "":
                    exit()
                calc = calcoprators(calc)
                y_input = input("second argument (press enter to finish): ")
                if y_input == "":
                    exit()
                y = float(y_input)
                result = print_result(calc, result, y)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()