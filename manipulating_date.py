from datetime import date


# Just Title.
print(' ')
print('Manipulating Date - Insert the year of birth of 7 people.')
print(' ')

# Define Variables.
actual_year = date.today().year
total_older = 0
total_minor = 0

# Looping - Asking for user year until 7 times.
for person in range(1, 8):

    born_year = int(input('Enter the year of birth of the {}° person: '.format(person)))
    person_age = actual_year - born_year

    # Older or Minor Test.
    if person_age >= 21:

        total_older += 1

    else:

        total_minor += 1

print(' ')
print('Altogether we had {} older people.'.format(total_older))
print('Altogether we had {} minor people.'.format(total_minor))
