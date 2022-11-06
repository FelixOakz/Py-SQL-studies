
"""
menu principal, ver pessoas cadastradas, cadastrar nova pessoa, sair
cadastro com nome e idade
defs: print linhas com texto dentro,
listar gente
menu
adiconar gente
"""

def writing(nome, idade):
	import os
	filepath = os.path.abspath('/Py-SQL-studies/random/TextDatabase.txt')
	file = open(filepath, 'a')
	file.write(f'{nome}, {idade}')
	file.close()

def reading():
	import os
	filepath = os.path.abspath('/Py-SQL-studies/random/TextDatabase.txt')
	file = open(filepath, 'r')
	file.read()


def printar(text):
	tam = len(text) + 4
	print(f'{"-"*tam}\n  {text}\n{"-"*tam}')

def separador(simb):
	print(f'{simb}'*30)





printar('MENU PRINCIPAL')
print('1 - Ver pessoas cadastradas')
print('2 - Cadastrar nova pessoa')
print('3 - Sair do sistema')