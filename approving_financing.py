#Approving bank financing for a House.

print('\033[0;30;43m FINANCING A HOUSE \033[m')
print(' ')

item_price = float(input('Insert the house price: € '))
client_age = int(input('How old are you? '))
client_sal = float(input('Insert your Monthly Salary: € '))
want_years = int(input('How many YEARS do you intend to pay? '))

line = 44
print('_' * line)
pc_max_sal = 30
part_times = want_years * 12
part_value = item_price / part_times
life_expec = 81

#The Salary Percentage condition
if (item_price / part_times) >= ((client_sal / 100) * pc_max_sal):
    print('The partial payment is: € {:.2f} per month.'.format(part_value))
    print('Its more than:     {}% (€ {:.2f}) of your monthly salary (€ {:.2f}).'.format(pc_max_sal, (client_sal / 100) * pc_max_sal, client_sal))
    print('\033[0;30;41m Sorry. Your salary is not adequate for this financing. \033[m')
    print(' ')

else:
    print('The partial payment is: € {:.2f} per month.'.format(part_value))
    print('Its less than:     {}% (€ {:.2f}) of your monthly salary (€ {:.2f}).'.format(pc_max_sal, ((client_sal / 100) * pc_max_sal), client_sal))
    print('\033[0;30;42m Your salary is adequate for this financing. \033[m')
    print(' ')

#The Life Expectancy condition
if client_age >= life_expec:
    print('\033[0;30;41m Sorry, your age group has not been approved. \033[m')
    print(' ')

if (life_expec * 12) - (client_age * 12) < (want_years * 12):
    print('In this country ...')
    print('The life expectancy is          {} years ({} months).'.format(life_expec, (life_expec * 12)))
    print('You are expected to live others {} years ({} months).'.format((life_expec - client_age), (life_expec * 12) - (client_age * 12)))
    print('This is less time than          {} years ({} months) that you intended to pay.'.format(want_years, (want_years * 12)))
    print('\033[0;30;41m Sorry, your age group has not been approved. \033[m')
    print(' ')

else:
    print('In this country ...')
    print('The life expectancy is          {} years ({} months).'.format(life_expec, (life_expec * 12)))
    print('You are expected to live others {} years ({} months).'.format((life_expec - client_age), (life_expec * 12) - (client_age * 12)))
    print('This is more time than          {} years ({} months) that you intended to pay.'.format(want_years, (want_years * 12)))
    print('\033[0;30;42m Your age group has been approved \033[m')
    print(' ')

print('Have a nice day')
