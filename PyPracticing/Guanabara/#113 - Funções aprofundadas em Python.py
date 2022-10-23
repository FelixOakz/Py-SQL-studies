def Leiaint(msg):
	while True:
		try:
			n = str(input(msg))
		except (ValueError, TypeError):
			print('Provavelmente vc digitou errado.')
			continue
		except KeyboardInterrupt:
			print('Usuario preferiu nao informar dados.')

		finally:
			return n
			print('Volte sempre! Muito obrigado!')


num = Leiaint('Digite um valor: ')
print(f'O valor digitado foi {num}')
