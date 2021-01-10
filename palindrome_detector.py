# Palindrome Detector.

phrase = str(input('Insert a phrase: ')).strip().upper()
words = phrase.split()
merge = ''.join(words)
reverse = ''

for letter in range(len(merge) -1, -1, -1):

    reverse = reverse + merge[letter]

if reverse == merge:

    print(' ')
    print('Its a palindrome!')

else:

    print(' ')
    print('It is not a palindrome!')

print(' ')
print("""Ty these great palindromes in Portuguese:

    1. socorram me subi no onibus em marrocos
       ("Help me, I got on the bus in Morocco!")
    2. anotaram a data da maratona
       ("They wrote down the date of the marathon!")    
    4. a torre da derrota
       ("The tower of defeat.")
    3. o lobo ama o bolo
       ("The wolf loves the cake.")
    4. a sacada da casa 
       ("the balcony of the house.")
    5. apos a sopa
       ("after the soup.")""")
