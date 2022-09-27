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
print('='*30)
print('No.', 'NOME', 'MEDIA', sep='     ')
print('-'*30)
for i in (0, len(geral)):
	print(f'{i}     {geral[i][0]}     ')
print('-'*30)

#print(boletim formatado com nome e media)