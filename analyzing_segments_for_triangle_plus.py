#Analyzing segments for Isosceles Triangle.

print('\033[0;30;43m Analyzing segments for a triangle. \033[m')
print(' ')
seg1 = float(input('Insert the  first segment: '))
seg2 = float(input('Insert the second segment: '))
seg3 = float(input('Insert the second segment: '))
print(' ')

if seg1 < (seg2 + seg3) and seg2 < (seg1 + seg3) and seg3 < (seg1 + seg2):
    print('These segments can form a triangle', end='')
    if seg1 == seg2 == seg3:
        print(' \033[0;30;43m(Equilateral)\033[m.')
    elif seg1 != seg2 != seg3 != seg1:
        print(' \033[0;30;43m(Scalene)\033[m.')
    else:
        print(' \033[0;30;43m(Isosceles)\033[m.')

else:
    print ('These segments cannot form a triangle.')
