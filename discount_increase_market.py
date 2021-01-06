#Product, normal price, discount#

#Just for decoration in "print"
line = 75

#Checks whether the code entered is within the allowed range of the product list.#
while True:
    try:
        product = int(input('Type the product code (1 to 5): '))
        if not 0 <= product <= 5:
            raise ValueError('ERROR! Try another code.')
        break
    except ValueError as error:
        print(error)

#Checks whether the code entered is within the allowed range of the product list.#
while True:
    try:
        price = float(input('Type the normal price ($): '))
        if not 0 <= price <= 10000:
            raise ValueError('ERROR! Try another code.')
        break
    except ValueError as error:
        print(error)

#Discount Level Verification#
while True:
    try:
        discount = int(input('Type the discount value (%): ')) / 100
        if not 0 <= discount <= 100:
            raise ValueError('ERROR! Try another code.')
        break
    except ValueError as error:
        print(error)

#Increase Level Verification#
while True:
    try:
        increase = int(input('Type the increase value (%): ')) / 100
        if not 0 <= increase <= 1000:
            raise ValueError('ERROR! Try another code.')
        break
    except ValueError as error:
        print(error)


#Product code
#1 = 1 + 'Choco'
#2 = 2 + 'Coke'
#3 = 3 + 'Book'
#4 = 4 + 'Bread'
#5 = 5 + 'Vodka'

price_descount = price - (price * discount)
price_increase = price + (price * increase)
print('-' * line)
print('\033[4;30;42m DISCOUNT: \033[m Product {} cost $ {:.2f}, with {:.0f}% off.'.format(product, price_descount, discount * 100))
print('\033[4;30;41m INCREASE: \033[m Product {} cost $ {:.2f}, with {:.0f}% increase.'.format(product, price_increase, increase * 100))
print('-' * line)