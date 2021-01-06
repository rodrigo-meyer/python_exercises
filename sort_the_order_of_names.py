#Sort the order of names#

from random import shuffle

print('Insert 4 names, separating them with Enter.')

n1 = str(input('\033[0;31;40m 1 \033[m '))
n2 = str(input('\033[0;31;40m 2 \033[m '))
n3 = str(input('\033[0;31;40m 3 \033[m '))
n4 = str(input('\033[0;31;40m 4 \033[m '))

list = [n1, n2, n3, n4]
shuffle(list)

print('_' * 33)
print('The order is: ',(list))
print('_' * 33)