n = 6
k = 3
ar = [1, 3, 2, 6, 1, 2]


def divisibleSumPairs(n, k, ar):
	pair = 0
	for i in ar:
		print(i)
		for j in ar:
			print(j)
			if (i + j) % k == 0:
				pair += 1
	print(pair)