def counter(start, end, step):
"""
a counting function and prints on screen:
Start parameter: beginning of counter
end parameter: end of couting
step parameter: step of counting
return: no return
"""
	c = start
	while c <= end:
		print(f'{end}', end='')
		c += step
	print('Finished.')

