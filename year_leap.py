#Analyzing Year Leap, including actual date from user computer.

from datetime import date

print('\033[0;30;43m DATE ANALYZER \033[m')
print(' ')
year = int(input('Type a year (yyyy): '))

#Reading the actual date from user computer.
if year ==0:
    year = date.today().year

if year %4 ==0 and year %100 != 0 or year % 400 == 0:
    print('Year {} is leap.'.format(year))
else:
    print('Year {} is not a leap.'.format(year))