numeros = []
pares = []
impares = []
for i in range(1, 8):
	numeros.append(int(input(f'Digite o {i} valor: ')))
for i in numeros:
	if i % 2 == 0:
		pares.append(i)
	else:
		impares.append(i)
pares.sort()
impares.sort()
print(f'Numeros pares foram {pares}')
print(f'Numeros impares foram {impares}')
