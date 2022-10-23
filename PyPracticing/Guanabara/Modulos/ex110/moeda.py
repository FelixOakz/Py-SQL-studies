def aumentar(p, val, formato=False):
	res = p + (p * val / 100)
	return res if formato is False else moeda(res)


def diminuir(p, val, formato=False):
	res = p - (p * val / 100)
	return res if formato is False else moeda(res)


def dobro(p, formato=False):
	res = p * 2
	return res if not formato else moeda(res)


def metade(p, formato=False):
	res = p / 2
	return res if not formato else moeda(res)


def moeda(val):
	return f'R${val:.2f}'

def resumo(p, plus=0, less=0):
	print('-'*30)
	print('RESUMO DO VALOR')
	print('-' * 30)
	print(f'Preco analisado eh de {moeda(p)}')
	print(f'O dobro do preco equivale a {dobro(p, True)}')
	print(f'A metade do preco equivale a {metade(p, True)}')
	print(f'Aumentando em {plus} o valor equivale a {aumentar(res)}')
	print(f'Aumentando em {less} o valor equivale a {diminuir(res)}')
