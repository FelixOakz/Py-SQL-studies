numeros = [[], []]
v = 0
for i in range(1, 8):
	v = int(input(f'Digite o {i} valor: '))
for i in numeros:
	if i % 2 == 0:
		numeros[0].append(i)
	else:
		numeros[1].append(i)

print(f'Numeros pares foram {pares}')
print(f'Numeros impares foram {impares}')
