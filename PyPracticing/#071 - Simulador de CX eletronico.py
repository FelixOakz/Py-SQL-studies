print('-'*30)
print(f"{'BDB - Banco dos Brothers':^30}")
print('-'*30)
notas50 = notas20 = notas10 = notas1 = 0
while True:
    valor = int(input('Insira o valor que deseja sacar(R$): '))
    while valor >= 50:
        valor -= 50
        notas50 += 1
    while valor >= 20:
        valor -= 20
        notas20 += 1
    while valor >= 10:
        valor -= 10
        notas10 += 1
    while valor >= 1:
        valor -= 1
        notas1 += 1
    break
print(f'\n> Lhe serao entregues {notas50} notas de R$50,\n'
      f'{notas20} notas de R$20,\n'
      f'{notas10} notas de R$10,\n'
      f'{notas1} notas de R$1. Bom dia!')
