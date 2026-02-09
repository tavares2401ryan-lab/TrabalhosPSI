# Dicionário que guarda os alunos da turma
# Cada aluno tem faltas, faltas de material e faltas disciplinares
turma = {}

# Função para pedir e validar o nome do aluno
def pedir_nome():
    nome = input("Nome do aluno: ").strip()

    # Verifica se o nome contém apenas letras (permite espaços)
    if not nome.replace(" ", "").isalpha():
        print("Erro: o nome deve conter apenas letras.")
        return None

    # Devolve o nome formatado com a primeira letra maiúscula
    return nome.title()

# Função para adicionar um aluno à turma
def adicionar_aluno():
    nome = pedir_nome()
    if nome is None:
        return

    # Verifica se o aluno já existe
    if nome in turma:
        print("Aluno já existe!")
    else:
        # Cria o aluno com os contadores a zero
        turma[nome] = {
            "faltas": 0,
            "material": 0,
            "disciplinar": 0
        }
        print("Aluno adicionado com sucesso.")

# Função para remover um aluno da turma
def remover_aluno():
    nome = pedir_nome()
    if nome is None:
        return

    if nome in turma:
        del turma[nome]
        print("Aluno removido.")
    else:
        print("Aluno não encontrado.")

# Função para listar todos os alunos e os seus dados
def listar_alunos():
    # Verifica se a turma está vazia
    if not turma:
        print("Não há alunos registados.")
        return

    # Percorre todos os alunos e mostra os dados
    for nome, dados in turma.items():
        print(f"""
Aluno: {nome}
  Faltas: {dados['faltas']}
  Falta de material: {dados['material']}
  Falta disciplinar: {dados['disciplinar']}
        """)

# Função para marcar uma falta normal
def marcar_falta():
    nome = pedir_nome()
    if nome is None:
        return

    if nome in turma:
        turma[nome]["faltas"] += 1
        print("Falta registada.")
    else:
        print("Aluno não encontrado.")

# Função para marcar falta de material
def falta_material():
    nome = pedir_nome()
    if nome is None:
        return

    if nome in turma:
        turma[nome]["material"] += 1
        print("Falta de material registada.")
    else:
        print("Aluno não encontrado.")

# Função para marcar falta disciplinar
def falta_disciplinar():
    nome = pedir_nome()
    if nome is None:
        return

    if nome in turma:
        turma[nome]["disciplinar"] += 1
        print("Falta disciplinar registada.")
    else:
        print("Aluno não encontrado.")

# Função principal do menu
def menu():
    while True:
        print("""
--- GESTOR DE TURMA ---
1 - Adicionar aluno
2 - Remover aluno
3 - Listar alunos
4 - Marcar falta
5 - Falta de material
6 - Falta disciplinar
0 - Sair
        """)

        opcao = input("Escolha uma opção: ")

        # Verifica se a opção é um número
        if not opcao.isdigit():
            print("Erro: introduza apenas números.")
            continue

        # Estrutura de decisão para escolher a opção
        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            remover_aluno()
        elif opcao == "3":
            listar_alunos()
        elif opcao == "4":
            marcar_falta()
        elif opcao == "5":
            falta_material()
        elif opcao == "6":
            falta_disciplinar()
        elif opcao == "0":
            print("A sair do programa...")
            break
        else:
            print("Opção inválida!")

# Início do programa
menu()
