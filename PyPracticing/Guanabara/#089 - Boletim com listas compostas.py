geral = []
temp = []
r = ''

while r in 'Ss':
	temp.append(str(input('Nome: ')))
	temp.append(int(input('Nota 1: ')))
	temp.append(int(input('Nota 2: ')))
	temp.append((temp[1] + temp[2])/2)
	geral.append(temp[:])
	temp.clear()
	r = str(input('Deseja adicionar mais um? [s/n]: '))

print('='*30, 'No.''NOME''MEDIA', '='*30, sep='\n')

for i in range(len(geral)):
	print(f'{i} {geral[i][0]}{geral[i][3]}')
print('-'*30)

while True:
	if r == 999:
		print('Programa Boletim Encerrado')
		break
	else:
		r = int(input('Mostrar notas de qual aluno?: '))
		print(F'>>> As notas de {geral[r][0]} sao {geral[r][1]} e {geral[r][2]}')
		print('-' * 30)