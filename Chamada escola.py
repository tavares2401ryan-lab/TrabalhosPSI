# =========================================
# MINI PROJETO - LISTA DE CHAMADA
# =========================================

# Lista que armazena os nomes dos alunos
alunos = []

# Dicionário que guarda a presença de cada aluno
# Exemplo: {"João": "Presente"}
presencas = {}

# Variável que controla o menu
opcao = "0"

# Enquanto a opção for diferente de 5, o programa continua rodando
while opcao != "5":

    # Exibição do menu principal
    print("\n==============================")
    print("   LISTA DE CHAMADA")
    print("==============================")
    print("1 - Adicionar aluno")
    print("2 - Remover aluno")
    print("3 - Marcar presença/falta")
    print("4 - Mostrar lista")
    print("5 - Sair")

    # Usuário escolhe uma opção do menu
    opcao = input("Escolha uma opção: ")

    # ---- VALIDAÇÃO: verifica se o usuário digitou apenas números ----
    # isdigit() retorna True se tudo for número
    if not opcao.isdigit():
        print("Erro: digite apenas números.")
        continue   # volta para o início do menu

    # -------- ADICIONAR ALUNO --------
    if opcao == "1":

        # Recebe o nome do aluno e remove espaços extras
        nome = input("Nome do aluno: ").strip()

        # ---- VALIDAÇÃO ----
        # replace(" ", "") remove espaços para permitir nomes compostos
        # isalpha() garante que só tenha letras
        # Também verifica se o aluno já não existe na lista
        if nome.replace(" ", "").isalpha() and nome not in alunos:

            # Adiciona o aluno na lista
            alunos.append(nome)

            # Define a presença inicial como "Não marcado"
            presencas[nome] = "Não marcado"

            print("Aluno adicionado com sucesso!")
        else:
            print("Erro: use apenas letras ou aluno já existe.")

    # -------- REMOVER ALUNO --------
    elif opcao == "2":

        # Solicita o nome do aluno que será removido
        nome = input("Nome do aluno a remover: ").strip()

        # Valida se o nome contém apenas letras e se o aluno existe
        if nome.replace(" ", "").isalpha() and nome in alunos:

            # Remove o aluno da lista
            alunos.remove(nome)

            # Remove também do dicionário de presenças
            del presencas[nome]

            print("Aluno removido.")
        else:
            print("Nome inválido ou aluno não encontrado.")

    # -------- MARCAR PRESENÇA --------
    elif opcao == "3":

        # Solicita o nome do aluno
        nome = input("Nome do aluno: ").strip()

        # Verifica se o nome é válido e existe na lista
        if nome.replace(" ", "").isalpha() and nome in alunos:

            # Mostra as opções de presença
            print("1 - Presença")
            print("2 - Falta")

            # Usuário escolhe presença ou falta
            escolha = input("Escolha: ")

            # ---- VALIDAÇÃO: verifica se digitou número ----
            if escolha.isdigit():

                # Se escolher 1, marca presença
                if escolha == "1":
                    presencas[nome] = "Presente"

                # Se escolher 2, marca falta
                elif escolha == "2":
                    presencas[nome] = "Falta"

                # Caso digite outro número
                else:
                    print("Opção inválida.")
            else:
                print("Erro: digite apenas números.")
        else:
            print("Nome inválido ou aluno não encontrado.")

    # -------- MOSTRAR LISTA --------
    elif opcao == "4":

        # Mostra todos os alunos e suas presenças
        print("\n--- LISTA DE CHAMADA ---")

        # Percorre a lista de alunos
        for aluno in alunos:
            # Mostra o nome do aluno e o status de presença
            print(aluno, "-", presencas[aluno])

    # -------- SAIR DO PROGRAMA --------
    elif opcao == "5":
        print("Saindo do programa...")

    # Caso o usuário digite um número fora das opções
    else:
        print("Opção inválida.")

