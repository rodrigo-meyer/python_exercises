# Working with Def.

def area_calc(a, b):

    text_bar("Area Calculator")
    a = float(input('Insert width  (m): '))
    b = float(input('Insert height (m): '))
    return_menu()


def return_menu():

    print('\nType \033[0;30;43m < \033[m to return to the menu')
    opt = str(input(''))

    if opt == '<':

        program()

    else:

        error_message()


def help_message():

    text_bar("Help Message")
    print("""
    An error message is sent whenever data is reported incorrectly or under
    conditions other than those expected. There is also the possibility of
    an unexpected program failure. If you think this was the case, please
    contact our support by email: suporte@email_fictional.com""")
    return_menu()


def error_message():

    msg = "You entered a wrong character."
    print(f'\033[0;30;41m {msg:^78} \033[m')
    hlp = str(input(f'Type \n\033[0;30;41m help \033[m for more info.\n')).upper()

    if hlp == 'HELP':

        help_message()

    else:

        error_message()


def end_message():

    text_bar("End")
    print('Program developed in Python 3.8, through the PyCharm interpreter.')


def menu_3opt(txt_1, txt_2, txt_3):

    print(f'\033[0;30;43m 1 \033[m {txt_1}')
    print(f'\033[0;30;43m 2 \033[m {txt_2}')
    print(f'\033[0;30;43m 3 \033[m {txt_3}')


def text_bar(txt):

    print(f'\n\033[0;30;43m {txt:^78} \033[m\n')


def program():

    text_bar("Working with Def.")
    menu_3opt("Calculate Area.", "Help.", "End.")

    option = int(input(''))

    if option == 1:

        area_calc(1, 2)

    elif option == 2:

        help_message()

    elif option == 3:

        end_message()

    else:

        error_message()


# Main Program
program()