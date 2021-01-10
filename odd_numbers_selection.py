# A program that calculates the sum between all the odd numbers
# that are multiples of 3 and that are in the range of 1 to 500.

# Variables.
adding = 0
counter = 0

for c in range(1, 501, 2):

    if c % 3 == 0:

        counter = counter + 1
        adding = adding + c

print('The total sum of {} values is {}'.format(counter, adding))
