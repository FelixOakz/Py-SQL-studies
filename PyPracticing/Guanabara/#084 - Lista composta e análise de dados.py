dados = []
galera = []

while True:
	dados.append(str(input('Qual seu nome?: ')))
	dados.append(str(input('Qual sua idade?: ')))
	galera.append(dados[:])
	dados.clear()
	r = input('Deseja continuar? [S/N]: ').strip()
	if r in 'Nn':
		break

print(galera)