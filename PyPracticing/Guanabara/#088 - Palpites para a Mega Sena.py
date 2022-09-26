from random import randint
from time import time

lista = []
print('-'*30, '        JOGOS NA MEGA','-'*30, sep='\n')
jogo = int(input('Quantod jogos voce quer?: '))

print(f'Sorteando {jogo} jogos.')
for i in range(jogo):
	for i in range(6):
		lista.append(randint(0, 60))

print('Jogo:', *lista)