m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
for i in range(0, 3):
	for j in range(0, 3):
		m[i][j] = int(input(f'Digite um valor para [{i}, {j}]:'))
for i in range(0, 3):
	for j in range(0, 3):
		print(f'[{m[i][j]:^5}]', end='')
	print()
print(f'A soma dos valores pares eh {par}')
print(f'A soma dos valores da segunda coluna eh de {}.')
print(f'O maior valor da segunda linha eh {}')
