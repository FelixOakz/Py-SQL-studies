geral = []
temp = []
r = ''
while r in 'Ss':
	temp.append(str(input('Nome: ')))
	temp.append(int(input('Nota 1: ')))
	temp.append(int(input('Nota 2: ')))
	geral.append(temp[:])
	temp.clear()
	r = str(input('Deseja adicionar mais um? [s/n]: '))


#print(boletim formatado com nome e media)