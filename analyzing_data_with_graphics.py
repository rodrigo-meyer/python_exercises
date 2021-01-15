# Analyzing Data with graphics.

# Program Variables.
prog_name = 'Life Goals.'
visual = ' '
# visual = '█'
# visual = '*'

g_size_goal = 0
g_size_actual = 0

print(f'\n\033[0;30;44m {prog_name:^52} \033[m\n')

while True:

    goal_name = str(input(f'Goal name: '))
    goal_value = int(input(f'Goal {goal_name}: '))
    actual_value = int(input(f'Actual {goal_name}: '))
    print('_' * 52)

    if goal_value or actual_value > 10000:

        goal_value = int(goal_value)
        g_size_goal = int(goal_value / 100)
        actual_value = int(actual_value)
        g_size_actual = int(actual_value / 100)

    elif goal_value or actual_value > 1000:

        goal_value = int(goal_value)
        g_size_goal = int(goal_value / 10)
        actual_value = int(actual_value)
        g_size_actual = int(actual_value / 10)

    elif goal_value or actual_value > 100:

        goal_value = int(goal_value)
        g_size_goal = int(goal_value / 1)
        actual_value = int(actual_value)
        g_size_actual = int(actual_value / 1)

    elif goal_value or actual_value > 10:

        goal_value = int(goal_value)
        g_size_goal = int(goal_value * 100)
        actual_value = int(actual_value)
        g_size_actual = int(actual_value * 100)

    print(f'  Goal {goal_name:<10} {goal_value:>10} \033[0;30;42m {visual * g_size_goal} \033[m\n')
    print(f'Actual {goal_name:<10} {actual_value:>10} \033[0;30;41m {visual * g_size_actual} \033[m')
    print('_' * 50)
    option = str(input('\033[0;30;44m Enter \033[m to add another or type \033[0;30;44m xxx \033[m to finish.')).upper()
    print('_' * 52)

    goal_value = 0
    actual_value = 0
    g_size_goal = 0
    g_size_actual = 0

    if option == ('XXX'):

        break

print(f'\n\033[0;30;45m {"":^44} \033[m\n\n')
