#Line Size in "Print" Decorations
line = 48

#Area Paint Statistics#
print('-' * line)
print('\033[4;30;43m What is the size of surface you want to paint? \033[m')

#Insertirg Area
width = float(input('Width surface (meter): '))
height = float(input('Height surface (meter): '))

#Inserting Price
print('-' * line)
print('\033[4;30;43m What is the price of paint? \033[m')
can_price = float(input('Can price (1,5 liters): '))
gal_price = float(input('Gallon price (5,0 liters): '))

#Variables
area = width * height
liters = area / 2
can_qt = liters / 1.5
gal_qt = liters / 5
can_qt_round = (liters / 1.5)
gal_qt_round = (liters / 5)

#Always Rounding up#
can_qt_round = round(can_qt_round + 0.5)
gal_qt_round = round(gal_qt_round + 0.5)

#Total Shop#
can_price_total = (can_price / 1.5) * liters
gal_price_total = (gal_price / 5) * liters

can_price_total_round = can_qt_round * can_price
gal_price_total_round = gal_qt_round * gal_price

print('-' * line)
print('For a \033[4;30;43m {} m² area \033[m you need a total of \033[4;30;43m {} liters \033[m'.format(area, liters))
print('This is \033[4;30;31m {:.1f} cans \033[m, that will pay: \033[4;30;31m {:.2f} \033[m. (n)ote that they will sell only \033[4;30;41m {:.0f} cans \033[m for \033[4;30;41m {} \033[m total price).'.format(can_qt, can_price_total, can_qt_round, can_price_total_round))
print('This is \033[4;30;31m {:.1f} gallons \033[m, that will pay: \033[4;30;31m {:.2f} \033[m. (n)ote that they will sell only \033[4;30;41m {:.0f} gallons \033[m for \033[4;30;41m {} \033[m total price).'.format(gal_qt, gal_price_total, gal_qt_round, gal_price_total_round))
print('-' * line)