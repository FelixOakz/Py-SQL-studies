lista = [input('Digite expressao: ')]
cont = 0
for x in lista:
    if '()' in lista:
        cont += 1
if cont % 2 == 0:
    print('Sua expressao esta valida')
if cont % 2 != 0:
    print('Sua expressao esta errada')
