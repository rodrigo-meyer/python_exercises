# Fibonacci Sequence

print('')
print('\033[0;30;43m Fibonacci Sequence. \033[m')
print('')

term1 = int(input('Insert the initial term (0 is traditional): '))
term2 = int(input('Insert the initial term (1 is traditional): '))
print('')
how_many = int(input('How many terms you want? '))

print('{}⊸{}'.format(term1, term2), end='')

counter = 3

while counter <= how_many:

    term3 = term1 + term2
    print('⊸{}'.format(term3), end='')
    term1 = term2
    term2 = term3
    counter += 1

print('⊸End.')
