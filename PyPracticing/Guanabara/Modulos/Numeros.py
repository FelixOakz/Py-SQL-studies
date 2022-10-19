def fatorial(n):
	f = 1
	for i in range(1, n+1):
		f *= i
	return f


num = int(input('Type a number to find its factorial: '))
print(f'Factorial of {num} equals {fatorial(num)}')