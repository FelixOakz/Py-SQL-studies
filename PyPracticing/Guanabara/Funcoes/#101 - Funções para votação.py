def voto(nasc):
	from datetime import date
	age = date.today().year - nasc
	if age < 18:
		print(f'Com {age} anos: NAO VOTA.')
	else:
		print(f'Com {age} anos: VOTO OBRIGATORIO.')


voto(int(input('what year were you born?: ')))
