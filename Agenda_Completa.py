AGENDA = {}

def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
            print("----------------------------")
    else:
        print(">>>>>>>>> Agenda Vazia")


def buscar_contato(contato):

    try:
        print("Nome:", contato)
        print("Telefone:", AGENDA[contato]['telefone'])
        print("Email:", AGENDA[contato]['email'])
        print("endereço:", AGENDA[contato]['endereco'])
    except KeyError:
        print(">>>>>>>>> Contato inecistente")
    except Exception as erro:
        print(">>>>>>>>> Ocorreu um erro inesperado")

def incluir_editar_contato(contato,telefone,email,endereco):

    AGENDA[contato] = {

        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar_contatos()
    print("----->>>>>>>>{} editado/adicionado com sucesso".format(contato))


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar_contatos()
        print(">>>>>>>>contato {} excluido com sucesso".format(contato))
    except KeyError:
        print(">>>>>>>> Contato inexistente")
    except Exception as erro:
        print(">>>>>>>> Erro inesoerado ocorreu")
        print(erro)

def exportar_contatos(nome_arquivo):
    try:
        with open(nome_arquivo, "w") as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]["telefone"]
                email  = AGENDA[contato]["email"]
                endereco = AGENDA[contato]["endereco"]
                arquivo.write("{},{},{},{}\n".format(contato,telefone,email,endereco))
        print("Contatos exportados com sucesso")
    except Exception as erro:
        print("Aconteceu um erro na execução do programa")
        print(erro)


def importar_contatos(nome_arquivo):

    try:
        with open(nome_arquivo,"r") as arquivo:
            ler = arquivo.readlines()
            for passar_ler in ler:
                dados_contato = (passar_ler.strip().split(","))
                contato = dados_contato[0]
                telefone = dados_contato[1]
                email = dados_contato[2]
                endereco = dados_contato[3]
                incluir_editar_contato(contato,telefone,email,endereco)
    except FileNotFoundError:
        print("Nenhum contato encontrato")
    except Exception as error:
        print("Algum erro inesperado ocorreu")
        print(error)


def carregar_contatos():
    try:
        with open("Banco_de_dados.csv", "r") as arquivo:
            ler = arquivo.readlines()
            for passar_ler in ler:
                dados_contato = (passar_ler.strip().split(","))

                contato = dados_contato[0]
                telefone = dados_contato[1]
                email = dados_contato[2]
                endereco = dados_contato[3]

                AGENDA[contato] = {

                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }
        print("Contatos carregados com sucesso")
    except FileNotFoundError:
        print("Nenhum contato encontrato")
    except Exception as error:
        print("Algum erro inesperado ocorreu")
        print(error)

def salvar_contatos():
    exportar_contatos("Banco_de_dados.csv ")

def imprimir_menu():
    print("-----------------------")
    print("1 - Mostrar todos os contatos da agenda")
    print("2 - Buscar contato")
    print("3 - incluir contato")
    print("4 - Editar contato")
    print("5 - Excluir contato")
    print("6 - Exportar contatos para CSV")
    print("7 - Importar contatos")
    print("0 - Fechar agenda")
    print("-----------------------")


carregar_contatos()
while True:

    imprimir_menu()

    opcao = input("Escolha uma opção: ")


    if opcao == "1":
        mostrar_contatos()
    elif opcao == "2":
        contato = input("Digite o nome do contato: ")
        buscar_contato(contato)
    elif opcao == "3":

        contato = input("Digite o nome do contato: ")

        try:
            AGENDA[contato]
            print(">>>>>> Contato existente")
        except KeyError:
            telefone = input("digire o numero do telefone: ")
            email = input("Difite o email: ")
            endereco = input("Digite o endereco: ")
            incluir_editar_contato(contato,telefone,email,endereco)

    elif opcao == "4":
        contato = input("Digite o nome do contato: ")

        try:
            AGENDA[contato]
            print(">>>>>> Editando contato: {}".format(contato))
            incluir_editar_contato(contato,telefone,email,endereco)
        except KeyError:
            print(">>>>>> Contato inexistente")

    elif opcao == "5":
        contato = input("Digite o nome do contato: ")
        excluir_contato(contato)

    elif opcao == "6":
        nome_arquivo = input("Digite o nome do arquivo a ser exportado: ")
        exportar_contatos(nome_arquivo)

    elif opcao == "7":

        nome_arquivo = input("Digite o nome do arquivo a ser importado: ")
        importar_contatos(nome_arquivo)

    elif opcao == "0":
        print("agenda fechada")
        break

    else:
        print("opção invalida")

