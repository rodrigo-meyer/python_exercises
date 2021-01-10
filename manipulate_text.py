# Manipulate text (incomplete at 05 jan 2021)

# Define Variables
name = str(input('Insert a full person name: ')).strip()
name_split = name.split()

if ' ' in name:

    print(' ')
    print('\033[0;30;44m    Considered: \033[m {}, {}, {}, {}'.format(name, name.upper(), name.lower(), name.title()))
    print('\033[0;30;43m        Length: \033[m {} characters (including spaces)'.format(len(name)))
    print('\033[0;30;43m                \033[m {} characters (without spaces)'.format(len(name)-(name.count(' '))))
    print('\033[0;30;44m   Composed by: \033[m {}'.format(name_split))
    print('\033[0;30;43m    First Name: \033[m {} characters: {}'.format(len(name_split[0]), name_split[0]))
    print('\033[0;30;43m     Last Name: \033[m {} characters: {}'.format(len(name_split[len(name_split)-1]), name_split[1]))

else:
    print('Single name is not allowed. Try again.')