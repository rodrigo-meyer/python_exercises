# Encrypting Alphabet to Number in this mode: 'a' for '1' until 9 and repeating.

# Modules from Python.
import re

# Title
print(' ')
print('\033[0;30;43m                                      NUMEROLOGY 1.0                                    \033[m')
print(' ')

# Encrypting Text in Alphabet to Number.
print("""\033[0;30;44m 1 2 3 4 5 6 7 8 9 \033[m 
 A B C D E F G H I
 J K L M N O P Q R
 S T U V W X Y Z
 """)

# Define Variables
alpha_latin = str(input('\033[0;30;43m name:  \033[m '))

# Any character to upper case.
alpha_latin = alpha_latin.upper()

# Letters.
alpha_latin = re.sub('A', '1', alpha_latin)
alpha_latin = re.sub('B', '2', alpha_latin)
alpha_latin = re.sub('C', '3', alpha_latin)
alpha_latin = re.sub('D', '4', alpha_latin)
alpha_latin = re.sub('E', '5', alpha_latin)
alpha_latin = re.sub('F', '6', alpha_latin)
alpha_latin = re.sub('G', '7', alpha_latin)
alpha_latin = re.sub('H', '8', alpha_latin)
alpha_latin = re.sub('I', '9', alpha_latin)
alpha_latin = re.sub('J', '1', alpha_latin)
alpha_latin = re.sub('K', '2', alpha_latin)
alpha_latin = re.sub('L', '3', alpha_latin)
alpha_latin = re.sub('M', '4', alpha_latin)
alpha_latin = re.sub('N', '5', alpha_latin)
alpha_latin = re.sub('O', '6', alpha_latin)
alpha_latin = re.sub('P', '7', alpha_latin)
alpha_latin = re.sub('Q', '8', alpha_latin)
alpha_latin = re.sub('R', '9', alpha_latin)

alpha_latin = re.sub('S', '1', alpha_latin)
alpha_latin = re.sub('T', '2', alpha_latin)
alpha_latin = re.sub('U', '3', alpha_latin)
alpha_latin = re.sub('V', '4', alpha_latin)
alpha_latin = re.sub('W', '5', alpha_latin)
alpha_latin = re.sub('X', '6', alpha_latin)
alpha_latin = re.sub('Y', '7', alpha_latin)
alpha_latin = re.sub('Z', '8', alpha_latin)

# Show the result (letters in respective numbers).
print('result:  {}'.format(alpha_latin))
print(' ')
print("""Please, add each number and add the result until you have a 1-digit number. In the next
version the numbers will be converted from Text to Integer Numbers and then added
together automatically.""")
