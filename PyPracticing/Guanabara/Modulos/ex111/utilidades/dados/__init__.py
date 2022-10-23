def readvalue(msg):
	valido = False
	while not valido:
		ent = str(input(msg)).replace(',', '.')
		if ent.isalpha() or ent.strip() == '':
			print(f'\033[0;31mERROR {ent}: Invalid command.\033[m')
		else:
			valido = True
			return float(ent)
