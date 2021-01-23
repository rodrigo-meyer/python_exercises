import webbrowser

# Este menino adora coisas coloridas!
search_original = str(input("\nSearch in "
                            "\033[1;34mG\033[m"
                            "\033[1;31mo\033[m"
                            "\033[1;33mo\033[m"
                            "\033[1;34mg\033[m"
                            "\033[1;32ml\033[m"
                            "\033[1;31me\033[m: "))

search_final = search_original.replace(" ", "+")

webbrowser.open(f'https://www.google.com/search?source=hp&ei=YnMFYMXUBN-65OUPsMG7-A8&iflsig=AINFCbYAAAAAYAWBcgw480xl4AqRRlfEZHsOeFPd8nH-&q={search_final}')
