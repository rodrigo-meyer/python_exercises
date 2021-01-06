#Sort a name from a pre-existing list.

from random import choice

print('Enter \033[0;30;43m 4 \033[m names, separating them with \033[0;30;43m Enter. \033[m.')

print('_' * 33)
n1 = str(input('\033[0;30;43m 1 \033[m '))
n2 = str(input('\033[0;30;43m 2 \033[m '))
n3 = str(input('\033[0;30;43m 3 \033[m '))
n4 = str(input('\033[0;30;43m 4 \033[m '))
print('_' * 33)

list = [n1, n2, n3, n4]

result = choice(list)

print('The chosen name was \033[0;30;43m {} \033[m.'.format(result))