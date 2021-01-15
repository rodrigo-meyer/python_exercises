# Analyzing Data with graphics.

# Program Variables.
prog_name = 'Life Goals.'
visual = ' '
# visual = '█'
# visual = '*'

size = 0

print(f'\n\033[0;30;44m {prog_name:^52} \033[m\n')

while True:

    goal_name = str(input(f'Goal name: '))
    goal_value = int(input(f'Goal {goal_name}: '))
    actual_value = int(input(f'Actual {goal_name}: '))
    print('_' * 52)

    if goal_value >= 9999 or actual_value >= 9999:

        goal_value = int(goal_value / 100000)
        actual_value = int(actual_value / 100000)

    elif goal_value >= 999 or actual_value >= 999:

        goal_value = int(goal_value / 1000)
        actual_value = int(actual_value / 1000)

    elif goal_value >= 99 or actual_value >= 99:

        goal_value = int(goal_value / 10)
        actual_value = int(actual_value / 10)

    print(f'Goal {goal_name:>8} {goal_value:>15} \033[0;30;42m {visual * goal_value} \033[m\n')
    print(f'Actual {goal_name:>6} {actual_value:>15} \033[0;30;41m {visual * actual_value} \033[m')
    print('_' * 50)
    option = str(input('\033[0;30;44m Enter \033[m to add another or type \033[0;30;44m xxx \033[m to finish.')).upper()
    print('_' * 52)

    goal_value = 0
    actual_value = 0

    if option == ('XXX'):

        break

print(f'\n\033[0;30;45m {"":^44} \033[m\n\n')
