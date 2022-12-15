arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
n = 3
primd = 0
secd = 0
for i in range(n):
	primd += arr[i][i]
	secd += arr[n - i - 1][i]
print(abs(primd - secd))