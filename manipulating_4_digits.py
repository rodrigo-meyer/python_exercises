#manipulating 4-digits

#"Convert To String" Mode:
num = int(input('\033[0;30;41m STRING MODE - Insert a 4-digit number between 0 and 9999: \033[m '))
num_convert = str(num)

print(' ')
print('Thousand: {} '.format(num_convert[0]))
print('Hundred:  {} '.format(num_convert[1]))
print('Tens:     {} '.format(num_convert[2]))
print('Unit:     {} '.format(num_convert[3]))
print(' ')

#Math Mode:
num = int(input('\033[0;30;41m MATH MODE --- Insert a 4-digit number between 0 and 9999: \033[m '))
print(' ')
thou = num // 1000 % 10
hund = num // 100 % 10
tens = num // 10 % 10
unit = num // 1 % 10

print('Thousand: {} '.format(thou))
print('Hundred:  {} '.format(hund))
print('Tens:     {} '.format(tens))
print('Unit:     {} '.format(unit))