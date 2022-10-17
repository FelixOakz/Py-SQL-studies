def ficha(nome='nao informado', gols=0):
	nome = str(input('Nome do jogador?: '))
	gols = int(input('Numero de gols?: '))
	print(f'O jogador {nome} fez {gols}gol(s) no campeonato')

ficha()