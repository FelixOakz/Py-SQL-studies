"""
ler idade e sexo de varias pessoas

a cada pessoa, o programa deve perguntar se quer ou nao continuar




e ao final mostre:
a) quantas pessoas com mais de 18 anos
b) quantos homens cadastrados
c) quantas Mulheres tem menos de 20 anos.

"""
maiores = homi = mulhermen = 0
while True:
    nom = str(input('Nome?: ')).strip()
    id = int(input('Idade?: '))
    sex = str(input('Sexo?: ')).strip().upper()[0]
    opt = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    if 'S' in opt:
        if id >= 18:
            maiores += 1
        elif sex == 'Mm':
            homi += 1
        elif sex == 'F' and id <= 20:
            mulhermen += 1
    else:
        break
print(f'\nDas pessoas entrevistadas, temos {maiores} maiores de idade,'
      f'{homi} Homens cadastrados,'
      f'E {mulhermen} mulheres com menos de 20 anos.')
