import webbrowser, pyperclip


def endereco_completo():
    info = input('\nInforme o seu endereço: ')
    return info


def cep():
    while True:
        info = input('\nInforme o CEP (O CEP deve possuir 8 dígitos): ')
        try:
            tamanho = len(info)
            if tamanho < 8 or tamanho > 8:
                print('>> Valor não permitido. Tente novamente.')
                continue
            info = int(info)
        except:
            print('>> Valor não permitido. Tente novamente.')
            continue
        cidade = input('\nInforme a cidade: ')
        info = str(info)
        inicio = info[:5]
        fim = info[5:]
        cep = inicio + '-' + fim
        busca = cep + ', ' + cidade
        break
    return busca


def resultado(opcao):
    if opcao == 1:
        info = endereco_completo()
        pyperclip.copy(info)
    else:
        info = cep()
        pyperclip.copy(info)

    endereco = pyperclip.paste()
    webbrowser.open('https://www.google.com/maps/place/' + endereco)


def menu():
    print('\n\t----MENU----')
    print('\nInforme um dos números correspondentes: ')
    print('\t1 - Buscar por endereço')
    print('\t2 - Buscar por CEP')
    while True:
        op = input('\nInforme o número de uma das opções acima: ')
        try:
            op = int(op)
            if op <= 0 or op >= 3:
                print('>> Valor não permitido. Tente novamente.')
                continue
            else:
                resultado(op)
            break
        except:
            print('>> Valor não permitido. Tente novamente.')
            continue


menu()
