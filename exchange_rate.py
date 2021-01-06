#Cotação Real, Dólar, Euro#

real = float(input('Digite um valor em Reais, R$: '))
cota_dolar = float(input('Defina a cotação diária do Dólar: '))
cota_euro = float(input('Defina a cotação diária do Euro: '))

dolar = float(real / cota_dolar)
euro = float(real / cota_euro)

line = 85

print('_' * line)
print('Com \033[4;30;43m R$ {:.2f} Reais \033[m você consegue comprar \033[4;30;41m US$ {:.2f} Dólares \033[m ou \033[4;30;44m € {:.2f} Euros \033[m'.format(real, dolar, euro))
print('_' * line)
print('Com \033[4;30;41m US$ {:.2f} Dólares \033[m você consegue comprar \033[4;30;43m R$ {:.2f} Reais \033[m ou \033[4;30;44m € {:.2f} Euros \033[m'.format(dolar, real, euro))
print('_' * line)
print('Com \033[4;30;44m € {:.2f} Euros \033[m você consegue comprar \033[4;30;43m R$ {:.2f} Reais \033[m ou \033[4;30;41m US$ {:.2f} Dólares \033[m'.format(euro, real, dolar))
print('_' * line)