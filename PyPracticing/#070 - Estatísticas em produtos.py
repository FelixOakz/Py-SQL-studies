tot = cont = prodB = prodC = 0
prodBNome = ' '
while True:
    produto = str(input('Digite o produto: ')).strip().upper()
    preco = int(input('Digite o valor do produto: '))

    tot += preco

    if preco > 1000:
        prodC += 1

    if preco < prodB:
        prodB = preco
        prodBNome = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'\n- - - Resumo da Compra - - -')
print(f'O total da compra foi de R${tot:.2f}')
print(f'Temos {prodC} produtos custando mais de R$1000')
print(f'O produto mais barato foi {prodBNome} que custa R${prodB}')
