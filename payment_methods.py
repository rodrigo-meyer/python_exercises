# Payment Methods
print(' ')
print('\033[0;30;43m                              BASIC MARKET                              \033[m')
print(' ')

# Clean Total and Input price.
total = 0
price = float(input('Insert the regular price: € '))

# User type a Method
print(' ')
print("""Select a payment method.
\033[0;30;43m 1. \033[m cash
\033[0;30;43m 2. \033[m card 1x
\033[0;30;43m 3. \033[m card 2x
\033[0;30;43m 4. \033[m card 3x or more
\033[0;30;43m 5. \033[m help
""")
method = int(input())

# Method Cash.
if method == 1:
    total = price - (price * 10 / 100)
    print('Cash')
    print('This method gives you 10% off')
    print('Regular Price: € {:.2f}'.format(price))
    print('\033[0;30;42m Total: € {:.2f} \033[m'.format(total))

# Method Card 1x.
elif method == 2:
    total = price - (price * 5 / 100)
    print('Card 1x')
    print('This method gives you 5% off')
    print('Regular Price: € {:.2f}'.format(price))
    print('\033[0;30;42m Total: € {:.2f} \033[m'.format(total))

# Method Card 2x.
elif method == 3:
    total = price
    print('Card 2x')
    print('This method has no increase or discount.')
    print('Regular Price: € {:.2f}'.format(price))
    print('\033[0;30;42m Price: € {:.2f} \033[m'.format(total))

# Method Card 3x or more.
elif method == 4:
    total = price + (price * 20 / 100)
    card_times = int(input('How many times to split card? '))
    print('Card 3x or more')
    print('This method increase 20% in total.')
    print('Regular Price: € {:.2f}'.format(price))
    print('\033[0;30;42m Total: € {:.2f} in {} x € {:.2f} \033[m'.format(total, card_times, (total / card_times)))

# Method Help.
elif method == 5:
    help_phrase = 'I WANT MY GREEN TOAST.'
    print("""If you need help for financial, medical, psychiatric,
    governmental assistance or want to discreetly signal
    that you are being kidnapped, say \033[0;30;43m "{}" \033[m
    and our staff will step in to help you.""".format(help_phrase))

# Wrong Method.
else:
    price = 0
    total = 0
    print('\033[0;30;41m ERROR (Method): \033[m This Payment Method does not exist. Try again.')
    print('\033[0;30;43m Total: € {:.2f} \033[m'.format(total))
