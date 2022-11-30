n = 9875987598759875
k = 0

n = int(n)
k += 1
while n > 9:
	n = sum(map(int, str(n)))
print(k)