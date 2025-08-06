from functions import *

list1 = []
list2 = []

def main():
    print("Welcome in calculator, enter your arguments:")
    try:

        x = get_arg("First argument (number or comma-separated list): ")
        calc = get_calc()
        y = get_arg("Second argument (number or comma-separated list): ")

        result = print_result(calc, x, y)

        while True:
            calc = input("calculation method (press enter to finish): ").strip()
            if not calc:
                break
            calc = calcoprators(calc)
            y = get_arg("second argument (can be a list or number) (press enter to finish): ")
            new_result = print_result(calc, result, y)
            if new_result is not None:
                result = new_result

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()