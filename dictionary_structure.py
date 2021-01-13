# Trying a English Dictionary.

# Purpouse Alert.
print("""
This code is for demonstration purposes
only. As a result, only 2 words were 
added. In a real situation, the words 
should need to be fed through a database
and not directly into the code. Try the
words 'car' and 'love'.
""")

#Variables
title = 'English Dictionary'
s = '↑'
search = 0

# Title.
print(f"""
\033[0;30;44m   \033[m \033[0;30;41m {title:^26}\033[m \033[0;30;44m   \033[m 
""")

# The visual structure of any result.
def item(means1, word1, lang1, word2, lang2, word3, lang3, word4, lang4, word5, lang5):


    print(f"""
{means1}

{word1:^33}
\033[0;30;41m {lang1:^33} \033[m
{s:^33}
{word2:^33}
\033[0;30;45m {lang2:^33} \033[m
{s:^33}
{word3:^33}
\033[0;30;44m {lang3:^33} \033[m 
{s:^33}
{word4:^33}
\033[0;30;43m {lang4:^33} \033[m
{s:^33}
{word5:^33}
\033[0;30;42m {lang5:^33} \033[m
""")


if search == 0:

    # User insert a word to search and code convert to uppercase.
    search = str(input("Search: ")).upper()

    # If user type CAR.
    if search == 'CAR':

        item("a four-wheeled road vehicle that is \npowered by an engine and is able\nto carry a small number of people.", 'car', 'English', 'car', 'Late Middle English', 'carre', 'Old Northern French', 'carrum, carrus', 'Latin', 'carrus', 'Celtic')

    # If user type LOVE.
    elif search == 'LOVE':

        item("1: an intense feeling of deep \naffection. 2: a great interest \nand pleasure in something.", 'love', 'English', 'lufu', 'Old English', 'lufu', 'Germanic', '.', 'Indo-European root', 'lubhyati', 'Sanskrit')

    else:

        print('Word not found')