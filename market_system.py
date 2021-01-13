# Market System.

market_name = 'Mega Shop'

# Euro
cipher = '€'

# Pound
# cipher = '£'

# American Dollar
# cipher = 'US$'

# Real
# cipher = 'R$'

# Generich Cipher
# cipher = '$'

line = 44
counter = 0
special_count = 0
special_price = float(1000.00)

shipest_price = 0
shipest_price_x = 0
shipest_name = ''

total = 0
name = ''
end_word = '!'
next = ''


print(f"""
\033[0;30;41m {market_name:^44} \033[m
""")

while next != end_word:

    name = str(input('product: '))
    price = float(input(f'price: {cipher} '))
    x = int(input('x '))
    counter += 1
    print(f'Press \033[0;30;43m Enter \033[m to continue or type \033[0;30;43m {end_word} \033[m to finish and show the total.')
    print('_' * line)
    next = str(input(''))
    total += price * x

    if price >= special_price:

        special_count +=1

    if counter == 1 or price < shipest_price:

        shipest_price = price
        shipest_price_x = x
        shipest_name = name

    if next == end_word:

        break

print(f'\033[0;30;42m Total: \033[m {cipher} {total:.2f}')
print(' ')
print('Note:')
print(f'{special_count} products costing more than {cipher} {special_price:.2f}')
print(f'Shipest product: {shipest_name}, {cipher} {shipest_price:.2f} x {shipest_price_x}')
