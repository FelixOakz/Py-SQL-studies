def writing(nome, idade):
    import os
    filepath = os.path.abspath('cevdatabase.txt')
    file = open(filepath, 'a')
    file.write(f'\n{nome}, {idade}')
    file.close() 


def reading():
    import os
    filepath = os.path.abspath('cevdatabase.txt')
    file = open(filepath, 'r')
    print(file.read())


def printar(text):
    print('-'*30)
    print(text)
    print('-'*30)


def separador(simb):
    print(f'{simb}'*30)


printar('     MENU PRINCIPAL')
print('1 - Ver pessoas cadastradas')
print('2 - Cadastrar nova pessoa')
print('3 - Sair do sistema')
while True:
    option = int(input('Escolha opcao: '))
    if option == 1:
        reading()
  
    elif option == 2:
        nome = str(input('Digite o nome: ')).strip().capitalize()
        idade = int(input('Digite a idade: '))
        writing(nome, idade)
    
    elif option == 3:
        printar('Saindo do sistema....')
        break
    else:
        print('Escolha uma opcao adequada!')
