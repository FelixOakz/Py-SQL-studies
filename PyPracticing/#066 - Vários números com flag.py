'''
ler varios numeros inteiros pelo teclado
so parar quando user digitar condic. parada: 999
final mostrar quantos n digitados e soma entre eles (sem o flag)
'''
cont = som = 0
while True:
    num = int(input('Digite um numero inteiro: '))
    cont += 1
    som += num
    if num == 999:
        break
print(f'Foram digitados {cont} numeros e a soma entre eles resulta em {som-999}')
