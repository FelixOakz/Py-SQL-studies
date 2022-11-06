import os

filepath = os.path.abspath('/Py-SQL-studies/random/TextDatabase.txt')

for i in range(1, 1001):
	file = open(filepath, 'a')
	file.write(f'teste numero {i}\n')
	file.close()

print('process finished')



"""
menu principal, ver pessoas cadastradas, cadastrar nova pessoa, sair
cadastro com nome e idade
defs: print linhas com texto dentro,
listar gente
menu
adiconar gente
"""

def printar(text):
	tam = len(text) + 4
	print(f'{"-"*tam}\n  {text}\n{"-"*tam}')

def

