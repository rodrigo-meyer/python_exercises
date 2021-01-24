from os import system
from time import sleep
from sys import version

interpreter = "Python " + version[version.find('3.'):5]
editor = "PyCharm Community"

class colors:
    header = '\n\033[43m'
    warning = '\n\033[94m'
    error = '\n\033[96m'
    fail = '\n\033[92m'
    end = '\033[0m'

menu = ["Calculate Area", "Help", "Quit"]

help_text = "An error message is sent whenever data is reported incorrectly " \
            "or under conditions other than those expected. There is also the " \
            "possibility of an unexpected program failure. If you think this " \
            "was the case, please contact our support by email: " \
            "suporte@email_fictional.com."
end_text = f"End\n Program developed with {interpreter} and {editor}."
error_text = "You entered a wrong option."
error_calc = "You entered an invalid input."


# Prints text to the shell
def print_it(color, text, b_size):
    print(f'{color}{text:^{b_size}}{colors.end}')
    sleep(3)


# Returns the area in m2
def area_calc(a, b):
    return a * b


# Shows menu
def show_menu():
    menu_text = "Select an option:\n"
    print(menu_text)
    for idx, item in enumerate(menu):
        print(str(idx + 1) + " - " + item)


def show_calculation():
    try:
        n1 = input("First integer: ")
        n2 = input("Second integer: ")
        txt = "The calculated area is: " + str(area_calc(int(n1), int(n2)))
        print_it(colors.fail, txt, 78)
    except:
        print_it(colors.error, error_calc, 78)
        system('clear')

print_it(colors.header, "Welcome to the area calculator!", 78)

while True:
    show_menu()
    try:
        option = int(input("Type a number: "))
        if option > len(menu) or option < 1:
            raise exception
    except:
        print_it(colors.error, error_text, 78)
        system('clear')

    if option == 1:
        show_calculation()
    elif option == 2:
        print_it(colors.warning, help_text, 78)
    elif option == 3:
        print_it(colors.end, end_text, 78)
        break