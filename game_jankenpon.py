# Jankenpo Game.

#Modules from Python
from random import randint
from time import sleep

# Title
print(' ')
print('\033[0;30;43m                                    JANKENPON  1.0                                  \033[m')
print(' ')

# The Game & Rules.
print("""\033[0;30;45m JANKENPON \033[m is a japanese game. It consists of two participants (in this case, the
computer and the user), where they must choose between ROCK, PAPER, SCISSOR. The one
who presents an option that dominates the opponent's option wins the game.
\033[0;30;44m   RULES   \033[m 1. scissor cut paper, 2. rock broken scissor, 3. paper wraps rock.
""")

# Options Examples to user.
print('\033[0;30;43m                         \033[m \033[0;30;43m 1. ROCK \033[m \033[0;30;43m 2. PAPER \033[m \033[0;30;43m 3. SCISSOR \033[m \033[0;30;43m                        \033[m ')
print(' ')

# Define Variables.
item = ('ROCK', 'PAPER', 'SCISSOR')
comp = randint(0, 2)
username = str(input('username: '))
user = int(input('choice: '))

#Initial Score Value.
score_user = 0
score_comp = 0

# Visual Delay Effect & Score.
print('         JAN!')
sleep(1)
print('             KEN!')
sleep(1)
print('                 PON!')
sleep(1)

#Compare Computer vs User choice for ROCK.
if comp == 0:

    if user == 0:
        print('\033[0;30;43m A TIE. \033[m')
    elif user == 1:
        print('\033[0;30;42m YOU WIN! \033[m')
        score_user =+1
        score_comp =+0
    elif user == 2:
        print('\033[0;30;43m YOU LOOSE! \033[m')
        score_user =+0
        score_comp =+1
    else:
        print('Wrong option!')

#Compare Computer vs User choice for PAPER.
elif comp == 1:

    if user == 0:
        print('\033[0;30;45m YOU LOOSE! \033[m')
        score_user =+0
        score_comp =+1
    elif user == 1:
        print('\033[0;30;43m A TIE. \033[m')
    elif user == 2:
        print('\033[0;30;42m YOU WIN! \033[m')
        score_user =+1
        score_comp =+0
    else:
        print('Wrong option!')

#Compare Computer vs User choice for SCISSOR.
elif comp == 2:

    if user == 0:
        print('\033[0;30;42m YOU WIN! \033[m')
        score_user =+1
        score_comp =+0
    elif user == 1:
        print('\033[0;30;45m YOU LOOSE! \033[m')
        score_user =+0
        score_comp =+1
    elif user == 2:
        print('\033[0;30;43m A TIE. \033[m')
    else:
        print('Wrong option!')

# Show Computer vs User options, adding a username for user.
print(' ')
print('computer \033[0;30;44m {} \033[m \033[0;30;41m {} \033[m X \033[0;30;41m {} \033[m \033[0;30;44m {} \033[m {}.'.format(item[comp], score_comp, score_user, item[user], username))
print(' ')