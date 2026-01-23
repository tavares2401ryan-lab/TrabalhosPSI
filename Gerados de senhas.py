# GERADOR DE PALAVRA-PASSE SEGURA
# ==================================
# Programa que cria uma palavra-passe
# usando nome, ano de nascimento e frase
# Possui menu e funções para organizar o código
# ==================================


# ---------- FUNÇÃO PARA VALIDAR ANO ----------
def pedir_ano():
    ano = input("Digite o seu ano de nascimento: ")
    while ano.isdigit() == False:
        print("Erro: use apenas números.")
        ano = input("Digite o seu ano de nascimento: ")
    return ano


# ---------- FUNÇÃO PARA GERAR SIGLA DA FRASE ----------
def gerar_sigla(frase):
    sigla = ""
    nova_palavra = True

    for letra in frase:
        if nova_palavra == True and letra.isalpha():
            sigla = sigla + letra.upper()
            nova_palavra = False

        if letra == " ":
            nova_palavra = True

    return sigla


# ---------- FUNÇÃO PARA GERAR PASSWORD ----------
def gerar_password(nome, ano, frase):
    password = ""
    contador = 0

    # Alterna maiúsculas e minúsculas no nome
    for letra in nome:
        if letra.isalpha():
            if contador % 2 == 0:
                password = password + letra.upper()
            else:
                password = password + letra.lower()
            contador = contador + 1

    # Adiciona sigla da frase
    sigla = gerar_sigla(frase)
    password = password + sigla

    # Adiciona os números do ano
    for numero in ano:
        password = password + numero

    return password


# ---------- PROGRAMA PRINCIPAL ----------
print("GERADOR DE PALAVRA-PASSE SEGURA\n")

nome = ""
ano = ""
frase = ""
password = ""

opcao = 0

while opcao != 5:

    print("\n==============================")
    print(" MENU PRINCIPAL ")
    print("==============================")

    if nome != "":
        print("Nome:", nome)
    if ano != "":
        print("Ano:", ano)
    if frase != "":
        print("Frase:", frase)

    print("\n1 - Inserir / Atualizar dados")
    print("2 - Gerar palavra-passe")
    print("3 - Mostrar palavra-passe")
    print("4 - Limpar dados")
    print("5 - Sair")

    opcao = input("\nEscolha uma opção: ")

    while opcao.isdigit() == False:
        print("Erro: digite apenas números.")
        opcao = input("Escolha uma opção: ")

    opcao = int(opcao)

    # ---------- OPÇÃO 1 ----------
    if opcao == 1:
        print("\n--- INSERIR / ATUALIZAR DADOS ---")
        nome = input("Digite o seu nome: ")
        ano = pedir_ano()
        frase = input("Digite uma frase: ")
        print("Dados atualizados com sucesso!")

    # ---------- OPÇÃO 2 ----------
    elif opcao == 2:
        if nome == "" or ano == "" or frase == "":
            print("Erro: primeiro insira os dados.")
        else:
            password = gerar_password(nome, ano, frase)
            print("Palavra-passe gerada com sucesso!")

    # ---------- OPÇÃO 3 ----------
    elif opcao == 3:
        if password == "":
            print("Nenhuma palavra-passe gerada ainda.")
        else:
            print("Palavra-passe:", password)

    # ---------- OPÇÃO 4 ----------
    elif opcao == 4:
        nome = ""
        ano = ""
        frase = ""
        password = ""
        print("Todos os dados foram limpos.")

    # ---------- OPÇÃO 5 ----------
    elif opcao == 5:
        print("Programa encerrado. Até logo!")

    else:
        print("Opção inválida.")


