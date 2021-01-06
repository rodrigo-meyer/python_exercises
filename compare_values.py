#Compare values from user input.

a = int(input('Insert the 1st value: '))
b = int(input('Insert the 2nd value: '))
c = int(input('Insert the 3rd value: '))
greater = a
lowest = a
line = 50

print(' ')
print('\033[0;30;43m RESULT \033[m')

#Analyzing if the user input equal numbers.
if a == b:
    print('The first  number {:.0f} is the same of the second {:.0f}.'.format(a, b))
if a == c:
    print('The first  number {:.0f} is the same of the third  {:.0f}.'.format(a, c))
if b == c:
    print('The second number {:.0f} is the same of the third  {:.0f}.'.format(b, c))
print('_' * line)

#Define the greater value.
if a > b and a > c:
     greater = a
if b > a and b > c:
    greater = b
if c > b and c > a:
    greater = c
print('The greater value is {:.0f}.'.format(greater))
print('_' * line)

#Define the lowest value.
if a < b and a < c:
    lowest = a
if b < a and b < c:
    lowest = b
if c < b and c < a:
    lowest = c
print('The lowest value is {:.0f}.'.format(lowest))
print('_' * line)