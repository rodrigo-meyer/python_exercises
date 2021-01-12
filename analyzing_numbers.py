
numeral = 0
counter = 0
lowest = 0
highest = 0
adding = 0
more = 'S'

while more in 'Ss':

    print(' ')
    numeral = int(input('Insert a Integer Number: '))
    adding = adding + numeral
    counter += 1

    if counter == 1:

        lowest = highest = numeral

    else:

        if numeral > highest:

            highest = numeral

        if numeral < lowest:

            lowest = numeral

    more = str(input('Do you want to insert more? [S/N] '))

average = adding / counter

print(' ')
print('You typed \033[0;30;43m {} numbers \033[m and the \033[0;30;43m sum \033[m between them is \033[0;30;43m {:.2f} \033[m.'.format(counter, adding))
print(' ')
print('The \033[0;30;43m average \033[m between them is \033[0;30;43m {:.2f} \033[m.'.format(counter, average))
print(' ')
print('The \033[0;30;43m highest is {} \033[m and the \033[0;30;43m lowest is {} \033[m.'.format(highest, lowest))
