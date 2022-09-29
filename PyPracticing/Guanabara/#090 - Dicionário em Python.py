dict = {}
dict['nome'] = str(input('Qual nome?: '))
dict['media'] = float(input(f'Qual a media de {dict["nome"]}?: '))
print(f'Nome eh igual a {dict["nome"]}.\nMedia eh igual a {dict["media"]}.')
if dict['media'] > 7.5:
	print('Situacao eh igual a Aprovado.')
else:
	print('Situacao eh igual a Reprovado.')
