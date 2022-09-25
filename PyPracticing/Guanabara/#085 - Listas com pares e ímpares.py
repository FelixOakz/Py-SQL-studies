numeros = [[], []]
v = 0
for i in range(1, 8):
	v = int(input(f'Digite o {i} valor: '))
	if i % 2 == 0:
		numeros[0].append(v)
	else:
		numeros[1].append(v)
numeros.sort()
print(f'Todos os valores: {numeros}')
