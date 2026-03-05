def menu():
    while True:
        print("\n===== MENU =====")
        print("1 - Ver informações do evento")
        print("2 - Adicionar participante")
        print("3 - Ver participantes")
        print("4 - Alterar turma")
        print("5 - Remover participante")
        print("6 - Estatísticas")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_evento()

        elif opcao == "2":
            adicionar_participante()

        elif opcao == "3":
            ver_participantes()

        elif opcao == "4":
            alterar_turma()

        elif opcao == "5":
            remover_participante()

        elif opcao == "6":
            estatisticas()

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("❌ Opção inválida.")


menu()