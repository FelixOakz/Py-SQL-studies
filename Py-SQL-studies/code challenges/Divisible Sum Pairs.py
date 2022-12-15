k = 3
ar = [1, 3, 2, 6, 1, 2]

pair = 0
pairs = []
for i in ar:
	for j in ar:
		if (i + j) % k == 0:
			pairs.append([i,j])
			for x in pairs:
				if x.count() == 1:
					pair += 1
print(pair)