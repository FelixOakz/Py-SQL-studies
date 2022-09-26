m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
for i in range(0, 3):
	for j in range(0, 3):
		m[i][j] = int(input(f'Digite um valor para [{i}, {j}]:'))
for i in range(0, 3):
	for j in range(0, 3):
		print(f'[{m[i][j]:^5}]', end='')
		if m[i][j] % 2 == 0:
			par += m[i][j]
	print()
print(f'A soma dos valores pares eh {par}.')
print(f'A soma dos valores da terceira coluna eh de {m[0][2] + m[1][2] + m[2][2]}.')
print(f'O maior valor da segunda linha eh {max(m[1])}.')