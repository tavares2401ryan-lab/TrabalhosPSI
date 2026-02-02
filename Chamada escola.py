# =========================================
# MINI PROJETO - LISTA DE CHAMADA
# =========================================

alunos = []          # guarda os nomes dos alunos
presencas = {}       # guarda presença ou falta de cada aluno

opcao = "0"

while opcao != "5":
    print("\n==============================")
    print("   LISTA DE CHAMADA")
    print("==============================")
    print("1 - Adicionar aluno")
    print("2 - Remover aluno")
    print("3 - Marcar presença/falta")
    print("4 - Mostrar lista")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    # ---- VALIDAÇÃO: opção TEM de ser número ----
    if not opcao.isdigit():
        print("Erro: digite apenas números.")
        continue

    # -------- ADICIONAR ALUNO --------
    if opcao == "1":
        nome = input("Nome do aluno: ").strip()

        # ---- VALIDAÇÃO: nome só pode ter letras ----
        if nome.replace(" ", "").isalpha() and nome not in alunos:
            alunos.append(nome)
            presencas[nome] = "Não marcado"
            print("Aluno adicionado com sucesso!")
        else:
            print("Erro: use apenas letras ou aluno já existe.")

    # -------- REMOVER ALUNO --------
    elif opcao == "2":
        nome = input("Nome do aluno a remover: ").strip()

        # ---- VALIDAÇÃO: nome só letras ----
        if nome.replace(" ", "").isalpha() and nome in alunos:
            alunos.remove(nome)
            del presencas[nome]
            print("Aluno removido.")
        else:
            print("Nome inválido ou aluno não encontrado.")

    # -------- MARCAR PRESENÇA --------
    elif opcao == "3":
        nome = input("Nome do aluno: ").strip()

        if nome.replace(" ", "").isalpha() and nome in alunos:
            print("1 - Presença")
            print("2 - Falta")

            escolha = input("Escolha: ")

            # ---- VALIDAÇÃO: escolha só número ----
            if escolha.isdigit():
                if escolha == "1":
                    presencas[nome] = "Presente"
                elif escolha == "2":
                    presencas[nome] = "Falta"
                else:
                    print("Opção inválida.")
            else:
                print("Erro: digite apenas números.")
        else:
            print("Nome inválido ou aluno não encontrado.")

    # -------- MOSTRAR LISTA --------
    elif opcao == "4":
        print("\n--- LISTA DE CHAMADA ---")
        for aluno in alunos:
            print(aluno, "-", presencas[aluno])

    elif opcao == "5":
        print("Saindo do programa...")

    else:
        print("Opção inválida.")
