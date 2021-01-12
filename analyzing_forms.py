# Analyzing Forms.

# System Variable
max_menu = 13

# Country Variables
legal_age_country = 18

# Group Variables.
group_total = 0
group_older_age = 0
group_older_name = ''
group_younger_age = 0
group_younger_name = ''
group_age_total = 0
group_age_average = 0
group_age_average_man = 0
group_age_average_woman = 0

# Man Variables
man_total = 0
man_legal = 0
man_under = 0
man_older_age = 0
man_older_name = ''
man_younger_age = 0
man_younger_name = ''

# Woman Variables
woman_total = 0
woman_legal = 0
woman_under = 0
woman_older_age = 0
woman_older_name = ''
woman_younger_age = 0
woman_younger_name = ''

# Menu.
print("""
\033[0;30;41m System                         \033[m
\033[0;30;43m [ 0] \033[m close.
\033[0;30;43m [ 1] \033[m add a new person.
\033[0;30;41m Group                          \033[m
\033[0;30;43m [ 2] \033[m find older person.
\033[0;30;43m [ 3] \033[m find younger person.
\033[0;30;43m [ 4] \033[m find older man.
\033[0;30;43m [ 5] \033[m find younger man.
\033[0;30;43m [ 6] \033[m find older woman.
\033[0;30;43m [ 7] \033[m find younger woman.
\033[0;30;41m Man                            \033[m
\033[0;30;43m [ 8] \033[m count man.
\033[0;30;43m [ 9] \033[m count man in legal age.
\033[0;30;43m [10] \033[m count man underage.
\033[0;30;41m Woman                          \033[m
\033[0;30;43m [11] \033[m count woman.
\033[0;30;43m [12] \033[m count woman in legal age.
\033[0;30;43m [13] \033[m count woman underage.
\033[0;30;41m                                \033[m
""")

opt = int(input('type a option in menu: '))

if opt != 0:

    while opt == 1:

        # Add a new person.
        group_total += 1
        print(' ')
        print('------------------ {}° person ------------------'.format(group_total))
        name = str(input('Name: ')).strip()
        genre = str(input('Genre (m / f): '))
        age = int(input('Age: '))
        print('------------------------------------------------')
        print('Person successfully registered!')
        print('------------------------------------------------')

        # Menu 2 - Older person.
        if age > group_older_age:

            group_older_name = name
            group_older_age = age

        # Menu 3 - Younger person.
        if age <= group_older_age:

            group_younger_name = name
            group_younger_age = age

        # Menu 4 - Older Man.
        if age >= group_older_age and genre in 'Mm':

            man_older_name = name
            man_older_age = age

        # Menu 5 - Younger Man.
        if age < group_older_age and genre in 'Mm':

            man_younger_name = name
            man_younger_age = age

        # Error (print and logic). still
        # Menu 6 - Older Woman.
        if age > group_older_age and genre in 'Ff':

            woman_older_name = name
            woman_older_age = age

        # Menu 7 - Younger Woman.
        if age < group_older_age and genre in 'Ff':

            woman_younger_name = name
            woman_younger_age = age

        # Menu 8 - Count Man.
        if genre in 'Mm':

            man_total += 1

        # Menu 9 - Count Man in legal age.
        if genre in 'Mm' and age >= legal_age_country:

            man_legal += 1

        # Menu 10 - Count Man underage.
        if genre in 'Mm' and age < legal_age_country:

            man_under += 1

        # Menu 11 - Count Woman.
        if genre in 'Ff':

            woman_total += 1

        # Menu 12 - Count Woman in legal age.
        if genre in 'Ff' and age >= legal_age_country:

            woman_legal += 1

        # Menu 13 - Count Woman underage.
        if genre in 'Ff' and age < legal_age_country:

            woman_under += 1

        opt = int(input('type a option in menu: '))

    while group_total != 0 and opt <= max_menu:

        if opt == 2:

            # Menu 2 - Older Person.
            print('The older person is {}, {} years.'.format(group_older_name, group_older_age))

        if opt == 3:

            # Menu 3 - Younger Person.
            print('The younger person is {}, {} years.'.format(group_younger_name, group_younger_age))

        if opt == 4:

            # Menu 4 - Older Man.
            print('The older man is {}, {} years.'.format(man_older_name, man_older_age))

        if opt == 5:

            # Menu 5 - Younger Man.
            print('The younger man is {}, {} years.'.format(man_younger_name, man_younger_age))

        if opt == 6:

            # Error (logic)
            # Menu 6 - Older Woman
            print('This option is being reformed. Try the next option.')
            #print('The older woman is {}, {} years.'.format(woman_older_name, woman_older_age))

        if opt == 7:

            # Menu 7 - Younger Woman.
            print('The younger woman is {}, {} years.'.format(woman_younger_name, woman_younger_age))

        if opt == 8:

            # Menu 8 - Total Man.
            print('Total man is {}.'.format(man_total))

        if opt == 9:

            # Menu 9 - Total Man in legal age.
            print('Total man in legal age is {}.'.format(man_legal))

        if opt == 10:

            # Menu 10 - Total Man underage.
            print('Total man underage is {}.'.format(man_under))

        if opt == 11:

            # Menu 11 - Total Woman.
            print('Total woman is {}.'.format(woman_total))

        if opt == 12:

            # Menu 12 - Total Woman in legal age.
            print('Total woman in legal age is {}.'.format(woman_legal))

        if opt == 13:

            # Menu 13 - Total Woman underage.
            print('Total woman underage is {}.'.format(woman_under))

        opt = int(input('type a option in menu: '))

    else:

        while opt != (0, 1):

            print('\033[0;30;41m No data for this option. \033[m')

            break

else:

    print('\033[0;30;41m End. \033[m')
