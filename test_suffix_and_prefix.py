#Testing Suffix and Prefix

#PREFIX - Analyze if the city name starts with "San".

city = str(input('\033[0;30;43m Insert a city that begins with SAN: \033[m ')).strip()
print(city[:3].upper() == 'SAN')

#SUFIX - Analyze if the city name ends with "burg".

city2 = str(input('\033[0;30;43m Insert a city that ends with BURG: \033[m ')).strip()
print(city2[3:].upper() == 'BURG')