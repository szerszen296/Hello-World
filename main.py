from functions import *

calculations = []

def main():
    print("Welcome in calculator, enter your arguments:")
    try:
        x = get_number("first argument: ")
        calc = get_calc()
        y = get_number("second argument: ")
        result = print_result(calc, x, y)
        append_calculation(x, calc, y, result, calculations, True)

        while True:
            calc = input("calculation method (press enter to finish): ")
            if calc == "":
                exit()
            calc = calcoprators(calc)
            y = get_number("second argument (press enter to finish): ")
            if y == "":
                exit()
            new_result = print_result(calc, result, y)
            append_calculation(result, calc, y, new_result, calculations, False)
            result = new_result
            history(calculations)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()