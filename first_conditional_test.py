#Conditional message for people of different ages

user_lastname = str(input("What is your last name? "))
user_lastname = user_lastname.upper()
my_lastname = "MEYER"
line = 75

if user_lastname == 'MEYER':
    print('_' * line)
    print("Nice! I'm \033[0;30;42m {} \033[m too! It is possible that we are related.".format(user_lastname, my_lastname))
    print('_' * line)
else:
    print('_' * line)
    print("Your last name \033[0;30;42m {} \033[m is different from mine \033[0;30;42m {} \033[m.".format(user_lastname, my_lastname))
    print('_' * line)
print("See you later!")