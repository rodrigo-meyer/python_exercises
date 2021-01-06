#Defines whether a number is even or odd

number = int(input('Insert any integer number: '))
analyze = number % 2

print('_' * 50)

#All EVEN number have % 2.
#ALL ODD number have % 1.

if analyze == 0:
    print('The number \033[0;30;43m {} is EVEN \033[m.'.format (number))
else:
    print('The number \033[0;30;43m {} is ODD \033[m.'.format(number))
