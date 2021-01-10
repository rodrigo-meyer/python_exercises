# Adding only Even numbers.
print('Adding only Even numbers.')
print(' ')

# Variables
adding = 0
counter = 0

# Looping process for 6 timex.
for c in range(1, 7):

    num = int(input('Insert the {}° number: '.format(c)))
    if num % 2 == 0:

        adding = adding + num
        counter = counter + 1

print('You entered {} number(s) and sum was: {}.'.format(counter, adding))
