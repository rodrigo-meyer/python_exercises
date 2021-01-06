#Game - Guess the Number!
from random import randint

computer_number = randint(0, 5)

line = 25

print('\033[0;30;43m=-=\033[m' * line)
print('\033[1;38;43m                             GUESS THE NUMBER!                               \033[m')
print('\033[0;30;43m=-=\033[m' * line)
print(' ')
print('I am thinking in a number between 0 and 5. Try to guess!')
user_try = int(input(' '))

if user_try == computer_number:
    print('\033[0;30;43m Congrats! \033[m I had really thought of number {}'.format(computer_number))
else:
    print('Wrong! I thought in number {}, not number {}. Try again!'.format(computer_number, user_try))