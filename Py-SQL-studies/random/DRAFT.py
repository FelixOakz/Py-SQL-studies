try:
	a = int(input('Numerador: '))
	b = int(input('Denominador: '))
	r = a/b
except:
	print('Infelizmente tivemos um problema :(')
else:
	print(f'0 resultado é {r:.1f}')
finally:
	print('Volte sempre! Muito obrigado!')
 