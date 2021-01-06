#Analyzing Names in a Doc

#Test if a text contains variants of "Meyer",
# either together or separated from other characters.

name = str(input('\033[0;30;43m Type a text or your full name: \033[m ')).strip()
name = name.upper()
print(' ')
print('Your full name contains \033[0;30;43m MEYER \033[m ? {} because appears \033[0;30;43m {} times. \033[m'.format('MEYER' in name, name.count('MEYER')))
print('Your full name contains \033[0;30;43m MEIER \033[m ? {} because appears \033[0;30;43m {} times. \033[m'.format('MEIER' in name, name.count('MEIER')))
print('Your full name contains \033[0;30;43m MAYER \033[m ? {} because appears \033[0;30;43m {} times. \033[m'.format('MAYER' in name, name.count('MAYER')))
print(' ')
print('Your full name contains \033[0;30;43m MAIER \033[m ? {} because appears \033[0;30;43m {} times. \033[m'.format('MAIER' in name, name.count('MAIER')))
print('Your full name contains \033[0;30;43m MEIAR \033[m ? {} because appears \033[0;30;43m {} times. \033[m'.format('MEIAR' in name, name.count('MEIAR')))
print('Your full name contains \033[0;30;43m MAIAR \033[m ? {} because appears \033[0;30;43m {} times. \033[m'.format('MAIAR' in name, name.count('MAIAR')))
print(' ')
print('Your full name contains \033[0;30;43m MAYAR \033[m ? {} because appears \033[0;30;43m {} times. \033[m'.format('MAYAR' in name, name.count('MAYAR')))
print('Your full name contains \033[0;30;43m MAYA  \033[m ? {} because appears \033[0;30;43m {} times. \033[m'.format('MAYA' in name, name.count('MAYA')))
print('Your full name contains \033[0;30;43m MAIA  \033[m ? {} because appears \033[0;30;43m {} times. \033[m'.format('MAIA' in name, name.count('MAIA')))
print(' ')
