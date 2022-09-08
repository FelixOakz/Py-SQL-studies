#simular caixa eletronico:

#perguntar qual valor a ser sacado:

#programa informa quantas celulas de cada valor sera entregue, sendo disponivel 50, 20, 10, 1.

"""
calculate number of 50s, then, 20s, then 10s, then ones...
number of 50s: 50s = 50s - 10s * 25
number of 20s:

"""

print('-'*30)
print(f"{'BDB - Banco dos Brothers':^30}")
print('-'*30)

while True:
    valor = int(input('Insira o valor que deseja sacar(R$): '))
