from functions import *

list1 = []
list2 = []

def main():
    print("Welcome in calculator, enter your arguments:")
    try:
        list1 = list_input("list1 (comma separated numbers): ")
        list2 = list_input("list2 (comma separated numbers): ")
        x = get_arg("first argument (can be a list: list1, list2): ", list1, list2)
        calc = get_calc()
        y = get_arg("second argument (can be a list: list1, list2): ", list1, list2)
        result = print_result(calc, x, y)

        while True:
            calc = input("calculation method (press enter to finish): ")
            if calc == "":
                exit()
            calc = calcoprators(calc)
            y = get_arg("second argument (can be a list: list1, list2) (press enter to finish): ", list1, list2)
            result = print_result(calc, result, y)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()