n = 9875987598759875
k = 3

n = int(n)
while n > 9:
	n = sum(map(int, str(n)))
print(k)

x = ((int(n) % 9) * k) % 9
return x if x else 9

# ??????