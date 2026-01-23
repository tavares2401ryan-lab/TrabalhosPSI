# Mini Projeto 2 – Lista de Chamada de Professor

# Lista para armazenar os nomes dos alunos
alunos = []

def adicionar_aluno():
    nome = input("Digite o nome do aluno para adicionar: ")
    alunos.append(nome)
    print(f"{nome} foi adicionado à lista.\n")

def remover_aluno():
    nome = input("Digite o nome do aluno para remover: ")
    if nome in alunos:
        alunos.remove(nome)
        print(f"{nome} foi removido da lista.\n")
    else:
        print(f"{nome} não está na lista.\n")

def listar_alunos():
    if alunos:
        print("Lista de alunos:")
        for i, aluno in enumerate(alunos, start=1):
            print(f"{i}. {aluno}")
        print()
    else:
        print("A lista de alunos está vazia.\n")

def procurar_aluno():
    nome = input("Digite o nome do aluno para procurar: ")
    if nome in alunos:
        print(f"{nome} está na lista.\n")
    else:
        print(f"{nome} não está na lista.\n")

def menu():
    while True:
        print("=== Lista de Chamada ===")
        print("1. Adicionar aluno")
        print("2. Remover aluno")
        print("3. Listar alunos")
        print("4. Procurar aluno")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_aluno()
        elif escolha == "2":
            remover_aluno()
        elif escolha == "3":
            listar_alunos()
        elif escolha == "4":
            procurar_aluno()
        elif escolha == "5":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida, tente novamente.\n")

# Executa o programa
menu()
