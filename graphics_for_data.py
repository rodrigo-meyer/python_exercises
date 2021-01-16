# Analyzing Data with graphics.

# Program Variables.
prog_name = 'Life Goals.'
visual = ' '
# visual = '█'
# visual = '*'
line = 60

g_size_goal = 0
g_size_actual = 0

print(f'\n\033[0;30;44m {prog_name:^60} \033[m\n')

while True:

    goal_name = str(input(f'Goal name: '))
    goal_value = int(input(f'Goal {goal_name}: '))
    actual_value = int(input(f'Actual {goal_name}: '))
    print('_' * 60)

    goal_value = int(goal_value)
    actual_value = int(actual_value)
    g_size = int(goal_value)
    a_size = int(actual_value)

    while g_size and a_size >= 20:

        g_size = int(g_size / 2)
        a_size = int(a_size / 2)

    print(f'  Goal {goal_name:<10} {goal_value:>10} \033[0;30;42m {visual * g_size} \033[m\n')
    print(f'Actual {goal_name:<10} {actual_value:>10} \033[0;30;41m {visual * a_size} \033[m')
    print('_' * line)
    option = str(input('\033[0;30;44m Enter \033[m to add another or type \033[0;30;44m xxx \033[m to finish.')).upper()
    print('_' * line)

    goal_value = 0
    actual_value = 0
    g_size = 0
    a_size = 0

    if option == ('XXX'):

        break

print('End.')
