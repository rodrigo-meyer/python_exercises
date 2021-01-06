import random

#Just a decorative line for "print".
line = 54

#Draw numbers between 0 and 60 and give 6 samples without repetition.
lot = random.sample(range(0, 60), 6)

print('_' * line)
print('Lottery Numbers Suggestion: \033[4;30;41m {} \033[m'.format(lot))
print('_' * line)

#Random subject to repetition.

#num1 = random.randint(1, 60)
#num2 = random.randint(1, 60)
#num3 = random.randint(1, 60)
#num4 = random.randint(1, 60)
#num5 = random.randint(1, 60)
#num6 = random.randint(1, 60)

#print('Lottery Numbers Suggestion: \033[4;30;41m {} \033[m \033[4;30;41m {} \033[m \033[4;30;41m {} \033[m \033[4;30;41m {} \033[m \033[4;30;41m {} \033[m \033[4;30;41m {} \033[m' .format(num1, num2, num3, num4, num5, num6))