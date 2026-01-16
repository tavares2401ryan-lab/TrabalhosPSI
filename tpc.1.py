print("==========================================")
print("        SISTEMA DE SEGURANÇA")
print("     Geração de Siglas e Passwords")
print("==========================================")
print("Acesso controlado por dados do utilizador")
print("==========================================")


# ------------------------------------------
# FUNÇÃO: MOSTRAR MENU
# ------------------------------------------
def mostrar_menu():
    print("\n============== MENU ==============")
    print("1 - Gerar SIGLA (a partir do nome)")
    print("2 - Gerar PASSWORD FORTE (série favorita)")
    print("3 - Ver última password gerada")
    print("4 - Ver força da password")
    print("5 - Ver regras de segurança")
    print("6 - Ajuda")
    print("7 - Sair")
    print("==================================")

# ------------------------------------------
# FUNÇÃO: GERAR SIGLA MAIS FORTE
# ------------------------------------------
def gerar_sigla(nome):
    partes = nome.split()
    sigla = ""

    for palavra in partes:
        primeira = palavra[0].upper()
        ultima = palavra[-1].lower()
        sigla += primeira + ultima

    sigla += str(len(nome))
    sigla += "#"

    return sigla

# ------------------------------------------
# FUNÇÃO: GERAR PASSWORD
# ------------------------------------------
def gerar_password(serie):
    texto = serie.replace(" ", "")
    password = ""

    if len(texto) >= 4:
        password = texto[:2] + "@2024!" + texto[-2:]
    else:
        password = texto + "@2024!"

    return password

# ------------------------------------------
# FUNÇÃO: VERIFICAR FORÇA
# ------------------------------------------
def verificar_forca(password):
    tamanho = len(password)

    if tamanho >= 12:
        return "FORTE"
    elif tamanho >= 8:
        return "MÉDIA"
    else:
        return "FRACA"

# ------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------
def main():

    ultima_password = ""
    ultima_forca = ""

    print("\nBem-vindo ao sistema!")
    print("Este programa ajuda a criar siglas e passwords.")

    while True:

        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        # ----------------------------------
        # OPÇÃO 1 - SIGLA
        # ----------------------------------
        if opcao == "1":
            print("\n--- GERAR SIGLA ---")
            nome = input("Digite o nome completo: ")

            if nome == "":
                print("Nome inválido.")
            else:
                sigla = gerar_sigla(nome)
                print("Sigla gerada:", sigla)

        # ----------------------------------
        # OPÇÃO 2 - PASSWORD
        # ----------------------------------
        elif opcao == "2":
            print("\n--- GERAR PASSWORD ---")
            serie = input("Qual sua série favorita? ")

            if serie == "":
                print("Série inválida.")
            else:
                password = gerar_password(serie)
                forca = verificar_forca(password)

                ultima_password = password
                ultima_forca = forca

                print("Password gerada:", password)
                print("Força:", forca)

        # ----------------------------------
        # OPÇÃO 3 - ÚLTIMA PASSWORD
        # ----------------------------------
        elif opcao == "3":
            print("\n--- ÚLTIMA PASSWORD ---")
            if ultima_password == "":
                print("Nenhuma password foi gerada ainda.")
            else:
                print("Última password:", ultima_password)

        # ----------------------------------
        # OPÇÃO 4 - FORÇA DA PASSWORD
        # ----------------------------------
        elif opcao == "4":
            print("\n--- FORÇA DA PASSWORD ---")
            if ultima_password == "":
                print("Nenhuma password disponível.")
            else:
                print("Força da última password:", ultima_forca)

        # ----------------------------------
        # OPÇÃO 5 - REGRAS
        # ----------------------------------
        elif opcao == "5":
            print("\n--- REGRAS DE SEGURANÇA ---")
            print("• Não usar apenas letras.")
            print("• Usar símbolos.")
            print("• Password maior que 8 caracteres.")
            print("• Não partilhar com ninguém.")

        # ----------------------------------
        # OPÇÃO 6 - AJUDA
        # ----------------------------------
        elif opcao == "6":
            print("\n--- AJUDA ---")
            print("Este sistema cria:")
            print("- Siglas baseadas no nome")
            print("- Passwords baseadas na série favorita")
            print("Use o menu para navegar.")

        # ----------------------------------
        # OPÇÃO 7 - SAIR
        # ----------------------------------
        elif opcao == "7":
            print("\nPrograma encerrado.")
            print("Obrigado por usar o sistema.")
            break

        else:
            print("\nOpção inválida. Tente novamente.")

# ------------------------------------------
# EXECUÇÃO DO PROGRAMA
# ------------------------------------------
if __name__ == "__main__":
    main()