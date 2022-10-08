"""
B) A média de idade do
grupo.
D) Uma lista com todas
as pessoas com idade acima da média.
"""

dict = {}
lista = []
age = 0
while True:
	dict['nome'] = str(input('Nome: '))
	dict['sexo'] = str(input('Sexo: ')).upper()[0]
	dict['idade'] = int(input('Idade: '))
	age += dict['idade']
	lista.append(dict.copy())
	r = str(input('Deseja continuar?[s/n]: ')).upper()[0]
	if r != 'S':
		break
print()
print(lista)
print()
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'A media de idade {age/len(lista):.1f}')
print(f'Lista com mulheres: ',end='')
for i in lista:
	if i['sexo'] == 'F':
		print(f'{i["nome"]}', end=' ')
print()
