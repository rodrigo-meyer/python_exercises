#This program calculates the value of the bus ticket,
# where trips over 200 km away have a lower price per kilometer.

print('\033[0;30;43m BUS TICKET \033[m')
print(' ')
distance = float(input('Insert the distance (km): '))

#Price per km, OVER 200 km distance.
price_short = 0.45
#Price per Km, BELOW 200 km distance.
price_long = 0.50

if distance <= 200:
    print('The total price is: \033[0;30;43m $ {:.2f} \033[m  ({:.2f} per km)'.format((price_long * distance), price_long))
else:
    print('The total price is: \033[0;30;43m $ {:.2f} \033[m ({:.2f} per km)'.format((price_short * distance), price_short))
print(' ')
print('Have a good travel!')