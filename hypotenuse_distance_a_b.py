from math import hypot

print('\033[4;30;43m Calculate the Hypotenuse or the distance between two points (vertical, horizontal). \033[m')

ver = float(input('Vertical distance (use same scale): '))
hor = float(input('Horizontal distance (use same scale): '))

distance = hypot(ver, hor)

print('The distance between the vertical point \033[4;30;43m {}\033[m and the horizontal point \033[4;30;43m {} \033[m is \033[4;30;43m {} \033[m'.format(ver, hor, distance))