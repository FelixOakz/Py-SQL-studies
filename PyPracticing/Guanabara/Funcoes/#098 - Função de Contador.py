def counter(start, end, step):
	print(f'Couting from {start} til {end} stepping {step}.')

	count = 0
	while count <= end:
		print(f'{count}', end='')
		count += step

counter(1, 10, 1)