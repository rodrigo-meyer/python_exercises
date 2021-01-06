#name = input('Name: ')
#gender = input('Gender (m/f): ')
#age = int(input('Age: '))
#weight = int(input('Weight (kg): '))
height = float(input('Height (cm): '))

ideal_weight_masc = int((height - 100) * 0.90)
ideal_weight_fem = int((height - 100) * 0.85)

max_masc = (ideal_weight_masc / 100) * 11.5 + (ideal_weight_masc)
max_fem = (ideal_weight_masc / 100) * 11.5 + (ideal_weight_fem)
print ('_' * 27)

print('For male, ideal weight is', ideal_weight_masc, 'to', int(max_masc), '.')
print('For female, ideal weight is', ideal_weight_fem, 'to', int(max_fem), '.')

#print('{}, {}, {} years old, {}, {}'.format (name, gender, age, weight, height)

#print('Hello {}, your ideal weight should be: {}'.format(name, ideal_weight)
#print('Hello {}, your ideal weight should be: {}'.format(name, ideal_weight)
#break