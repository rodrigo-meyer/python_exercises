#Using an angle, define the sine, cosine and tangent.#
#Two decimal places after the floating point.#

from math import radians, sin, cos, tan

angle = float(input('Insert a initial angle: '))

sine = sin(radians(angle))
print('For angle \033[4;30;43m {:.2f} \033[m, the sine is    \033[4;30;43m {:.2f} \033[m.'.format(angle, sine))

cosine = cos(radians(angle))
print('For angle \033[4;30;43m {:.2f} \033[m, the cosine is  \033[4;30;43m {:.2f} \033[m.'.format(angle, cosine))

tangent = tan(radians(angle))
print('For angle \033[4;30;43m {:.2f} \033[m, the tangent is \033[4;30;43m {:.2f} \033[m.'.format(angle, tangent))