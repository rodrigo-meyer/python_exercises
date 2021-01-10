# Selecting Odd or Even numbers. Example: 1 is a Odd number, 2 is a Even number.

# Best Code.
# Showing Odd Numbers between 0 and 50.
print(' ')
print('Best Code.')
print('Odd Numbers: ')

for n in range(1, 50, 2):

    print(n, end=' ')

print('End.')

# Best Code.
# Showing Even Numbers between 0 and 50.
print('Best Code.')
print('Even Numbers: ')

for n in range(2, 51, 2):

    print(n, end=' ')

print('End.')

"""Although the solutions below are not
the most efficient, they help to
illustrate the mathematical method for
finding odd and even numbers."""

# Normal Code.
# Showing Odd Numbers between 0 and 50.
print('Normal Code.')
print('Odd Numbers: ')

for n in range(0, 50):

    if n % 2 != 0:
        print(n, end=' ')

print('End.')

# Normal Code.
# Showing Even Numbers between 0 and 50.
print('Normal Code.')
print('Even Numbers: ')

for n in range(1, 51):

    if n % 2 == 0:

        print(n, end=' ')

print('End.')
