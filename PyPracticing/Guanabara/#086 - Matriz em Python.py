m = [[], [], []]
for i in range(0, 3):
	for j in range(0, 3):
		m[i].append(int(input(f'Digite um valor para [{i}, {j}]:')))
print(m[0])