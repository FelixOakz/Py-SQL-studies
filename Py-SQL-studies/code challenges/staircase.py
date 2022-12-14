def staircase(n):
	c = 1
	for i in range(n):
		print(f'{" "*n}{"#"*c}')
		n -= 1
		c += 1

if __name__ == '__main__':
	n = int(input().strip())

	staircase(n)