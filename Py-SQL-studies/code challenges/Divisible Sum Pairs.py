k = 3
ar = [1, 2, 3, 4, 5, 6]

pair = 0
for i in ar:
	for j in ar:
		if i < j and (i + j) % k == 0:
			pair += 1
print(pair)