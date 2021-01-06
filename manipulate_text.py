#Manipulate text (incomplete at 05 jan 2021)
name = str(input('Insert a name: ')).strip()
name_split = name.split()

line = 50
print(' ')
print('\033[0;30;44m    Considered: \033[m {}, {}, {}, {}'.format(name, name.upper(), name.lower(), name.title()))
print('\033[0;30;43m        Length: \033[m {} characters (including spaces)'.format(len(name)))
print('\033[0;30;43m                \033[m {} characters (without spaces)'.format(len(name)-(name.count(' '))))
print('\033[0;30;44m   Composed by: \033[m {}'.format(name_split))
print('\033[0;30;43m    First Name: \033[m {} characters: {}'.format(len(name_split[0]), name_split[0]))
print('\033[0;30;43m     Last Name: \033[m {} characvters: {}'.format(len(name_split[len(name_split)-1]), name_split[1]))

#Finding Vowels
name = name.lower()

vowel_a = name.find('a')
vowel_e = name.find('e')
vowel_i = name.find('i')
vowel_o = name.find('o')
vowel_u = name.find('u')
vowel_total = (vowel_a + vowel_e + vowel_i + vowel_o + vowel_u)

#Finding Consonants
name = name.lower()

consonant_b = name.find('b')
consonant_c = name.find('c')
consonant_d = name.find('d')
consonant_f = name.find('f')
consonant_g = name.find('g')
consonant_h = name.find('h')
consonant_j = name.find('j')
consonant_k = name.find('k')
consonant_l = name.find('l')
consonant_m = name.find('m')
consonant_n = name.find('n')
consonant_p = name.find('p')
consonant_q = name.find('q')
consonant_r = name.find('r')
consonant_s = name.find('s')
consonant_t = name.find('t')
consonant_v = name.find('v')
consonant_w = name.find('w')
consonant_x = name.find('x')
consonant_y = name.find('y')
consonant_z = name.find('z')
consonant_total = (consonant_b + consonant_c + consonant_d + consonant_f + consonant_g + consonant_h + consonant_j + consonant_k + consonant_l + consonant_m + consonant_n + consonant_p + consonant_q + consonant_r + consonant_s + consonant_t + consonant_v + consonant_w + consonant_x + consonant_y + consonant_z)

#Finding Number
name = name.lower()

number0 = name.find('0')
number1 = name.find('1')
number2 = name.find('2')
number3 = name.find('3')
number4 = name.find('4')
number5 = name.find('5')
number6 = name.find('6')
number7 = name.find('7')
number8 = name.find('8')
number9 = name.find('9')
number_total = (number1 + number2 + number3 + number4 + number5 + number6 + number7 + number8 + number9)

#Finding Space
name = name.lower()

space_total = name.find(' ')

print('\033[0;30;43m        Vowels: \033[m {}'.format(vowel_total))
print('\033[0;30;43m    Consonants: \033[m {}'.format(consonant_total))
#print('\033[0;30;43m       Numbers: \033[m {}'.format(number_total))
print('\033[0;30;43m        Spaces: \033[m {}'.format(space_total))
print('\033[0;30;44m      Initials: \033[m {}'.format(name[0:3]))
print('\033[0;30;43m  Jumping Mode: \033[m {}'.format(name[0::2]))
print(' ')

#Enconded Name Study
#name = name.lower()

#name_encoded = name.replace('r', '9')

#name_encoded = name.replace(('a', '1'),('b', '2'),('c', '3'),('d', '4'),('e', '5'),('f', '6'),('g', '7'),('h', '8'),('j', '9'),('k', '1'),('l', '2'),('m', '3'),('n', '4'),('o', '5'),('p', '6'), ('q', '7'),('r', '8'),('s', '9'),('t', '1'),('u', '2'),('v', '3'), ('w', '4'), ('x', '5'), ('y', '6'), ('z', '7'))
#print('Your encoded name is: {} '.format(name_encoded))

#print('\033[0;30;41m       Encoded: \033[m {}'.format(name_encoded))