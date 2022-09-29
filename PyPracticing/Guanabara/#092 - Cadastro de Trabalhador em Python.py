dict = {}
dict['nome'] = str(input('Qual o nome?: '))
dict['anoNascimento'] = int(input(f'Qual o ano de nascimento de {dict["nome"]}?: '))
dict['numCarteira'] = int(input(f'Qual numero da carteira de trabalho?(0 se nao tem): '))
if dict['numCarteira'] != 0:
	dict['anoContratacao'] = str(int(input(f'Qual ano de contratacao?: ')))
	dict['salario'] = int(input(f'Qual salario?:'))

