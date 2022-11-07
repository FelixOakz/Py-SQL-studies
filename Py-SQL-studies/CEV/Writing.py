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


if __name__ == '__main__':
    while True:
        option = input('Escolha opcao: ')
        if option == '1':
            reading()
    
        elif option == '2':
            nome = str(input('Digite o nome: ')).strip().capitalize()
            idade = int(input('Digite a idade: '))
            writing(nome, idade)
        
        elif option == '3':
            printar('Saindo do sistema....')
            break
        else:
            print('\033[0;31mEscolha uma opcao adequada!\033[m')
        