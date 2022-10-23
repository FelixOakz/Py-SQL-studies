def readvalue(msg):
	valido = False
	while not valido:
		ent = str(input(msg))
		if ent.isalpha():
			print(f'\033[0;31mERROR {ent}: Invalid command.\033[m')
		else:
			valido = True
			return float(ent)