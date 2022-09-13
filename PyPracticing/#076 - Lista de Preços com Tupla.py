"""
tupla com nome sde produtos e seus precos
no final uma lsitagem de precos, organizando os dados de forma tabular
"""
produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

print('-'*50)
print('LISTAGEM DE PRECOS')
print('-'*50)
for i in range(0, len(produtos), 2):
	print(f'{produtos[i]}', f'{produtos[i + 1]}')

