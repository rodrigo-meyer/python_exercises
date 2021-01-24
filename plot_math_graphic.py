import matplotlib.pyplot

# A list with time distance.
timex = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# A list with each value in time.
value = [30, 35, 47, 40, 55, 68, 60, 70, 75, 78, 77, 80]

# Graphic X-Y mechanism.
matplotlib.pyplot.plot(timex, value)

# Just labels for graphic.
matplotlib.pyplot.xlabel('Time')
matplotlib.pyplot.ylabel('Value')

# Show graphic on screen.
matplotlib.pyplot.show()

# You can add values to the list with input and append or both.

# Input method.
# user_timex = float(input('Insert a value : '))
# user_value = float(input('Insert a value : '))

# Append method.
# timex.append(user_timex)
# value.append(user_value)
