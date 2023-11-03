def timer(tempo):
    import time
    import sys

    if tempo == 10:
        print(f'Em {tempo} segundos o programa será fechado!')
        for i in range(0, tempo):
            sys.stdout.write("\r{}".format(i + 1))
            sys.stdout.flush()
            time.sleep(1)
        print('')

    elif tempo == 3:
        print(f'Em {tempo} segundos você voltará para fazer login!')
        print('-' * 100)
        for i in range(0, tempo):
            sys.stdout.write("\r{}".format(i + 1))
            sys.stdout.flush()
            time.sleep(1)
        print('')

    else:
        print(f'Em {tempo} segundos voltaremos para o menu incial...')
        for i in range(0, tempo):
            sys.stdout.write("\r{}".format(i + 1))
            sys.stdout.flush()
            time.sleep(1)
        print('')


def cpf_entrada():
    def validador_cpf(cpf):
        corpo_cpf = cpf[:9]
        digito_cpf = cpf[-2:]

        calculo_1 = 0
        calculo_2 = 0

        multiplicacao = [10, 9, 8, 7, 6, 5, 4, 3, 2]

        for i, j in zip(multiplicacao, corpo_cpf):
            calculo_1 += i * int(j)

        resto_1 = calculo_1 % 11

        digito_1 = 0 if resto_1 < 2 else 11 - resto_1

        corpo_cpf += str(digito_1)

        for i, j in zip(multiplicacao, corpo_cpf[1:]):
            calculo_2 += i * int(j)

        resto_2 = calculo_2 % 11

        digito_2 = 0 if resto_2 < 2 else 11 - resto_2

        return digito_cpf == f'{digito_1}{digito_2}'

    blocklist = [
        '00000000000',
        '11111111111',
        '22222222222',
        '33333333333',
        '44444444444',
        '55555555555',
        '66666666666',
        '77777777777',
        '88888888888',
        '99999999999'
    ]

    while True:
        cpf_inserido = input('Por favor digite seu CPF ou insira "X" para sair:')
        print('-' * 100)
        cpf_sem_barra = cpf_inserido.replace('-', '')
        cpf_formatado = cpf_sem_barra.replace('.', '')

        if cpf_formatado.isnumeric():
            if len(cpf_formatado) == 11:
                if cpf_formatado in blocklist:
                    print('O CPF não pode conter todos números iguais!\n')
                else:
                    if not validador_cpf(cpf_formatado):
                        print('Seu CPF está invalido\n')
                    else:
                        return cpf_formatado

            else:
                print('O CPF deve conter 11 dígitos!\n')

        elif cpf_formatado.lower() == 'x':
            return False

        else:
            print('Digite seu CPF corretamente ou apenas "x" para sair!\n')


def login():
    print('-' * 100)
    print('Bem vindo a RebocAI!')
    print('-' * 100)

    cpf_usuario = cpf_entrada()

    if cpf_usuario in segurados:
        return True

    elif cpf_usuario.lower() == 'x':
        return False

    else:
        cadastro(cpf_usuario)


def abertura_sinistro(id):
    import datetime
    import json

    def endereco_sinistro():
        while True:
            rua = input('Por favor digite a rua de onde o veiculo está: ')
            if rua.isnumeric():
                print('Por favor não utilize numeros na hora de digitar a rua! ')
            else:

                while True:
                    numero = input('Por favor digite o numero ou o km onde o veiculo esta: ')
                    if numero.isnumeric():
                        while True:
                            cep = input('Por favor digite seu cep: ')
                            cep_formatado = cep.replace('-', '')
                            if cep_formatado.isnumeric():
                                if len(cep_formatado) == 8:

                                    endereco = {
                                        'rua': rua,
                                        'numero': numero,
                                        'cep': cep
                                    }
                                    return endereco

                                else:
                                    print('O cep deve conter 8 digitos')

                            else:
                                print('Por favor utilize apenas numeros para digitar o cep!')
                    else:
                        print('Por favor utilize numeros na hora de informar o numero/km!')

    def tipo_sinistro():
        while True:
            escolha_usuario = input('Por favor escolha uma das opções acima: ')
            print('-' * 100)

            if escolha_usuario.isnumeric():
                if 5 > int(escolha_usuario) > 0:
                    return escolha_usuario

                else:
                    print('Escolha somente as opções listadas')
                    print('-' * 100)

            else:
                print('Por favor utilize números na escolha')
                print('-' * 100)

    print(f'Olá {segurados[id]["nome"]} verificamos que seu veiculo é um {segurados[id]["veiculo"]},'
          f' a altura do mesmo é de {segurados[id]["altura"]}M e sua Apolice é de {segurados[id]["apolice"]}.')

    print('-' * 100)
    print('Vamos começar com seu endereço!')
    endereco_usuario = endereco_sinistro()

    print('-' * 100)
    print('O que aconteceu com seu veiculo?: ')
    print('[1] - Pane eletrica;\n'
          '[2] - Capotamento;\n'
          '[3] - Desastre natural;\n'
          '[4] - Batida;\n')

    escolha_sinistro = tipo_sinistro()

    if escolha_sinistro == '1':
        print('-' * 100)
        print(f'Otimo! de acordo acordo com o modelo do seu veiculo: {segurados[id]["veiculo"]},'
              f'estamos enviando um mecanico que chegará em menos de 20 minutos de moto com uma nova bateria!')

        data = datetime.datetime.now()

        registrar_sinistro = {
            'tipo': 'Pane eletrica',
            'data': (str(data)),
            'endereco': endereco_usuario
            }
        registros['registro_sinistro'] = registrar_sinistro

        with open('registros.json', 'w') as file:
            json.dump(registros, file, indent=4)

        timer(4)
        return True



    elif escolha_sinistro == '2':
        print('Otimo! Seu veiculo estava carregado?\n[1] Sim\n[2] Não')

        while True:
            carregado = input('Por favor escolha uma das opções acima: ')
            print('-' * 100)

            if carregado.isnumeric():
                if carregado == '1':

                    while True:
                        peso = input('Por favor digite o peso da carga em toneladas: ')
                        if peso.isnumeric():
                            print('Ok! Estamos enviando um modal de acordo com o peso da sua carga!')

                            data = datetime.datetime.now()

                            registrar_sinistro = {
                                'tipo': 'Capotamento',
                                'peso_carga': peso,
                                'data': (str(data)),
                                'endereco': endereco_usuario
                            }
                            registros['registro_sinistro'] = registrar_sinistro

                            with open('registros.json', 'w') as file:
                                json.dump(registros, file, indent=4)

                            timer(4)
                            return True

                        else:
                            print('Por favor utilize apenas numeros para digitar o peso!')


                elif carregado == '2':
                    print(
                        f'Ok! Estamos mandando um Modal de acordo com o modelo do seu veiculo: '
                        f'{segurados[id]["veiculo"]}')
                    data = datetime.datetime.now()

                    registrar_sinistro = {
                        'tipo': 'Capotamento',
                        'data': (str(data)),
                        'endereco': endereco_usuario
                    }

                    registros['registro_sinistro'] = registrar_sinistro

                    with open('registros.json', 'w') as file:
                        json.dump(registros, file, indent=4)

                    timer(4)
                    return True

                else:
                    print('Escolha somente as opções listadas')
                    print('-' * 100)

            else:
                print('Por favor utilize números na escolha')
                print('-' * 100)

    elif escolha_sinistro == '3':
        print('Otimo! Seu veiculo estava carregado?\n[1] Sim\n[2] Não')

        while True:
            carregado = input('Por favor escolha uma das opções acima: ')
            print('-' * 100)

            if carregado.isnumeric():
                if carregado == '1':

                    while True:
                        peso = input('Por favor digite o peso da carga em toneladas: ')
                        if peso.isnumeric():
                            print('Ok! Estamos enviando um modal de acordo com o peso da sua carga!')

                            data = datetime.datetime.now()

                            registrar_sinistro = {
                                'tipo': 'Desastre natural',
                                'peso_carga': peso,
                                'data': (str(data)),
                                'endereco': endereco_usuario
                            }
                            registros['registro_sinistro'] = registrar_sinistro

                            with open('registros.json', 'w') as file:
                                json.dump(registros, file, indent=4)

                            timer(4)
                            return True

                        else:
                            print('Por favor utilize apenas numeros para digitar o peso!')


                elif carregado == '2':
                    print(
                        f'Ok! Estamos mandando um Modal de acordo com o modelo do seu veiculo:'
                        f' {segurados[id]["veiculo"]}')
                    data = datetime.datetime.now()

                    registrar_sinistro = {
                        'tipo': 'Desastre natural',
                        'data': (str(data)),
                        'endereco': endereco_usuario
                    }

                    registros['registro_sinistro'] = registrar_sinistro

                    with open('registros.json', 'w') as file:
                        json.dump(registros, file, indent=4)

                    timer(4)
                    return True

                else:
                    print('Escolha somente as opções listadas')
                    print('-' * 100)

            else:
                print('Por favor utilize números na escolha')
                print('-' * 100)

    elif escolha_sinistro == '4':
        print('Otimo! Seu veiculo estava carregado?\n[1] Sim\n[2] Não')

        while True:
            carregado = input('Por favor escolha uma das opções acima: ')
            print('-' * 100)

            if carregado.isnumeric():
                if carregado == '1':

                    while True:
                        peso = input('Por favor digite o peso da carga em toneladas: ')
                        if peso.isnumeric():
                            print('Ok! Estamos enviando um modal de acordo com o peso da sua carga!')

                            data = datetime.datetime.now()

                            registrar_sinistro = {
                                'tipo': 'Batida',
                                'peso_carga': peso,
                                'data': (str(data)),
                                'endereco': endereco_usuario
                            }
                            registros['registro_sinistro'] = registrar_sinistro

                            with open('registros.json', 'w') as file:
                                json.dump(registros, file, indent=4)

                            timer(4)
                            return True

                        else:
                            print('Por favor utilize apenas numeros para digitar o peso!')


                elif carregado == '2':
                    print(
                        f'Ok! Estamos mandando um Modal de acordo com o modelo do seu veiculo:'
                        f' {segurados[id]["veiculo"]}')
                    data = datetime.datetime.now()

                    registrar_sinistro = {
                        'tipo': 'Batida',
                        'data': (str(data)),
                        'endereco': endereco_usuario
                    }

                    registros['registro_sinistro'] = registrar_sinistro

                    with open('registros.json', 'w') as file:
                        json.dump(registros, file, indent=4)

                    timer(4)
                    return True

                else:
                    print('Escolha somente as opções listadas')
                    print('-' * 100)

            else:
                print('Por favor utilize números na escolha')
                print('-' * 100)


def dados_cadastro(item):
    if item == 'nome':
        while True:
            nome = input('Digite o seu primeiro nome: ')
            if nome.isnumeric():
                print('Não utilize numeros na hora de cadastrar o nome!')
            else:
                return nome

    elif item == 'veiculo':
        while True:
            veiculo = input('Digite o modelo do seu veiculo: ')
            if veiculo.isnumeric():
                print('Não utilize numeros na hora de cadastrar o veiculo!')
            else:
                return veiculo

    elif item == 'altura':
        while True:
            altura = input('Digite a altura do veiculo arredondada em metros: ')
            if altura.isnumeric():
                return altura
            else:
                print('Por favor não utilize letras na hora cadastrar a altura')

    elif item == 'placa':
        while True:
            placa = input('Digite o seu numero da placa: ')
            if len(placa) == 7:
                return placa
            else:
                print('Sua placa deve conter 7 digitos')

    elif item == 'numero':
        while True:
            numero = input('Digite o seu numero de telefone: ')
            if numero.isnumeric():
                return numero
            else:
                print('Por favor não utilize letras na hora cadastrar o seu número')


def cadastro(id):
    print('-' * 100)
    print('Percebemos que seu CPF não possui cadastro no nosso sistema!\n'
          'Iremos te cadastrar neste exato momento! ')
    print('-' * 100)

    segurados_cadastro = {
        'nome': dados_cadastro('nome'),
        'veiculo': dados_cadastro('veiculo'),
        'altura': dados_cadastro('altura'),
        'placa': dados_cadastro('placa'),
        'numero': dados_cadastro('numero'),
        'eixos': dados_cadastro('eixos'),
        'apolice': dados_cadastro('apolice')
    }

    segurados[id] = segurados_cadastro
    print('-' * 100)
    print((' ' * 30) + 'Seus dados foram cadastrados com sucesso!')
    print('-' * 100)
    timer(3)


def mostrar_dados(id):
    print(f'Seus dados cadastrados são:\n {segurados[id]}')
    print('-' * 100)


def alterar_dados(id):
  def escolha_dados():
    print('Escolha qual dado você deseja alterar: ')
    print('[0] - Nome;\n'
      '[1] - Veiculo;\n'
      '[2] - Altura do veiculo;\n'
      '[3] - Placa;\n'
      '[4] - Numero telefone;\n'
      '[5] - Eixos;\n'
      '[6] - Apolice;\n')
    while True:
        escolha_usuario = input('Por favor escolha a opção desejada: ')
        print('-' * 100)

        if escolha_usuario.isnumeric():
            if 7 > int(escolha_usuario) >= 0:
              lista = ['nome', 'veiculo', 'altura', 'placa', 'numero', 'eixos','apolice']
              return lista[int(escolha_usuario)]

            else:
                print('Escolha somente as opções listadas')
                print('-' * 100)

        else:
            print('Por favor utilize números na escolha')
            print('-' * 100)

  if id in segurados:
    print(f'Seus dados cadastrados são:\n {segurados[id]}')
    print('-' * 100)

    dado_para_mudar = escolha_dados()

    dado_alterado = dados_cadastro(dado_para_mudar)

    segurados[id][dado_para_mudar] = dado_alterado

def registro_sinistro():
  import json

  with open('registros.json', 'r') as file:
    sinistro = json.load(file)
    
  return sinistro


def menu_inicial():
    print('-' * 100)
    print((' ' * 30) + 'MENU INICIAL')
    print('-' * 100)
    print('[0] Sair\n'
          '[1] Solicitar sinistro\n'
          '[2] Mostrar dados cadastrados\n'
          '[3] Alterar dados cadastrados\n'
          '[4] Mostrar historico de sinistro')
    print('-' * 100)

    while True:
        escolha_usuario = input('Por favor escolha a opção desejada: ')
        print('-' * 100)

        if escolha_usuario.isnumeric():
            if 5 > int(escolha_usuario) >= 0:
                return escolha_usuario

            else:
                print('Escolha somente as opções listadas')
                print('-' * 100)

        else:
            print('Por favor utilize números na escolha')
            print('-' * 100)


segurados = {}
registros = {}

try:
    login()

except:
    print("Você escolheu sair!")
    timer(10)

else:
    while True:
        menu = menu_inicial()

        if menu == '0':
            print('-' * 100)
            print('Voce escolheu sair')
            print('-' * 100)
            timer(10)
            break

        elif menu == '1':
            id_cpf = cpf_entrada()
            if id_cpf in segurados:
                abertura_sinistro(id_cpf)
                timer(4)

            elif not id_cpf:
                continue
            else:
                print('-' * 100)
                print('Você não possui nenhum dado cadastrado neste CPF')


        elif menu == '2':
            id_cpf = cpf_entrada()
            if id_cpf in segurados:
                mostrar_dados(id_cpf)
                timer(4)

            elif not id_cpf:
                continue
            else:
                print('-' * 100)
                print('Você não possui nenhum dado cadastrado neste CPF')


        elif menu == '3':
            id_cpf = cpf_entrada()

            if id_cpf in segurados:
                alterar_dados(id_cpf)
                timer(4)

            elif not id_cpf:
                continue
            else:
                print('-' * 100)
                print('Você não possui nenhum dado cadastrado neste CPF')


        elif menu == '4':
            if len(registros) == 0:
                print('-' * 100)
                print('Você não realizou nenhum sinistro!')

            else:
                print(registro_sinistro())
                timer(4)

finally:
    print('-' * 100)
    print((' ' * 30) + 'Obrigado por usar a RebocAI! <3')
    print('-' * 100)