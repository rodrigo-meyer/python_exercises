# Treating singular or plural according to the number of items.

print('Treating singular or plural according to the number of items.')
print('')
num = int(input('Enter the amount of books you have (for Example: 0, 1, 2, 53): '))

print('You have {} book'.format(num), end='')
print('' if num == 1 else 's', end='.')
