n = 9875987598759875

n = int(n)
while n > 9:
	n = sum(map(int, str(n)))

print(n)