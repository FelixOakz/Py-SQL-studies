def ajuda(comando):
	import comando
	help(comando)


comando = ''
print('-'*25, '\n PYTHON INTERACTIVE HELP \n','-'*25)
while True:
	comando = str(input('Library or function: '))
	if comando.upper() == 'FIM':
		break
	else:
		ajuda(comando)
