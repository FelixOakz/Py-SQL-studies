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

notas50 = notas20 = notas10 = notas1 = 0
while True:

    valor = int(input('Insira o valor que deseja sacar(R$): '))
    while valor % 50:
        notas50 += 1
    break

print(f'\n> Serao entregues {notas50} notas de R$50,\n'
      f'{notas20} notas de R$20,\n'
      f'{notas10} notas de R$10,\n'
      f'{notas1} notas de R$1. Bom dia!'
      )
