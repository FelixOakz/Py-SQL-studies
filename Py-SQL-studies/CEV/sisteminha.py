def writing(nome, idade):
    try:
        import os
        filepath = os.path.abspath('cevdatabase.txt')
        file = open(filepath, 'a')
        file.write(f'\n{nome},{idade}')
        file.close()
    except IOError:
        print('\033[0;31mFile not found or path is incorrect!\033[m\n')


def reading():
    try:
        import os
        filepath = os.path.abspath('cevdatabase.txt')
        file = open(filepath, 'r')
        for linha in file:
            data = linha.split(',')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]:>3} anos')
        print(line())
    except IOError:
        print('\033[0;31mFile not found or path is incorrect!\033[m\n')


def line(tam = 42):
    return '-'* tam


def header(txt):
    print(line())
    print(txt.center(42))
    print(line())


def separador(simb):
    print(f'{simb}'*30)


if __name__ == '__main__':
    while True:
        option = input('Escolha opcao: ')
        print(line())
        if option == '1':
            reading()

        elif option == '2':
            header('cadastrar pessoa:')
            nome = str(input('Digite o nome: ')).strip().capitalize()
            idade = int(input('Digite a idade: '))
            writing(nome, idade)
        
        elif option == '3':
            header('Saindo do sistema')
            break
        else:
            print('\033[0;31mEscolha uma opcao adequada!\033[m')
