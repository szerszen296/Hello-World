from functions import *

calculations = []

def main():
    print("Welcome in calculator, enter your arguments:")
    try:
        x = get_number("first argument: ")
        calc = get_calc()
        append_calculation(x, calc, calculations, True)
        y = get_number("second argument: ")
        append_calculation(y, "=", calculations, False)
        result = print_result(calc, x, y)
        append_calculation("=", result, calculations, True)
        history(calculations)

        while True:
            calc = input("calculation method (press enter to finish): ")
            if calc == "":
                exit()
            calc = calcoprators(calc)
            append_calculation(result, calc, calculations, True)
            y = get_number("second argument (press enter to finish): ")
            if y == "":
                exit()
            append_calculation(y, "=", calculations, False)
            result = print_result(calc, result, y)
            append_calculation("=", result, calculations, True)
            history(calculations)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()