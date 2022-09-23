entrada = []
pessoas = []
cont = menor = maior = 0
while True:
	entrada.append(str(input('Qual seu nome?: ')))
	entrada.append(str(input('Qual seu peso?: ')))
	pessoas.append(entrada[:])
	cont += 1
	entrada.clear()
	r = str(input('Deseja continuar? [S/N]: ')).strip()
	if r in 'Nn':
		break
print('-'*40)
print(f'Os dados foram {pessoas}')
print(f'Ao todo, foram cadastradas {len(pessoas)} pessoas.')
#print(f'Maior peso foi de {}kg, peso de {}.')
#print(f'Menor peso foi de {}kg, peso de {}.')
