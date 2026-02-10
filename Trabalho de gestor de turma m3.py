import json
# Importa a biblioteca json
# Serve para guardar e carregar os dados num ficheiro


# --------------------------------------------------
# Dicionário principal da turma
# Cada aluno é uma "chave" e os valores são os registos
# --------------------------------------------------
turma = {}

# Nome do ficheiro onde os dados vão ser guardados
FICHEIRO = "turma.json"


# ==================================================
#                  UTILIDADES
# ==================================================

def pedir_nome():
    """
    Pede o nome do aluno ao utilizador.
    Verifica se só contém letras e espaços.
    """
    while True:  # Repete até o nome ser válido
        nome = input("Nome do aluno: ").strip()  # Remove espaços no início e fim

        # Remove espaços do nome e verifica se só tem letras
        if nome.replace(" ", "").isalpha():
            return nome.title()  # Coloca a primeira letra de cada palavra em maiúscula
        else:
            print("Erro: o nome deve conter apenas letras.")


def pedir_numero(mensagem):
    """
    Pede um número ao utilizador e valida a entrada.
    """
    while True:
        valor = input(mensagem)
        if valor.isdigit():  # Verifica se é um número
            return int(valor)
        print("Erro: introduza um número válido.")


# ==================================================
#                FICHEIROS (JSON)
# ==================================================

def guardar_dados():
    """
    Guarda o dicionário 'turma' num ficheiro JSON.
    """
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        # json.dump guarda os dados no ficheiro
        json.dump(turma, f, indent=4, ensure_ascii=False)

    print("Dados guardados com sucesso.")


def carregar_dados():
    """
    Carrega os dados do ficheiro JSON para o programa.
    Se o ficheiro não existir, começa com a turma vazia.
    """
    global turma  # Permite alterar a variável global

    try:
        with open(FICHEIRO, "r", encoding="utf-8") as f:
            turma = json.load(f)  # Lê os dados do ficheiro

        print("Dados carregados com sucesso.")
    except FileNotFoundError:
        # Se o ficheiro não existir
        print("Nenhum ficheiro encontrado. A começar vazio.")


# ==================================================
#                  ALUNOS
# ==================================================

def adicionar_aluno():
    """
    Adiciona um novo aluno à turma.
    """
    nome = pedir_nome()

    if nome in turma:  # Verifica se o aluno já existe
        print("Aluno já existe!")
    else:
        # Cria o aluno com os registos a zero
        turma[nome] = {
            "faltas": 0,
            "material": 0,
            "disciplinar": 0
        }
        print("Aluno adicionado com sucesso.")


def remover_aluno():
    """
    Remove um aluno da turma.
    """
    nome = pedir_nome()

    if nome in turma:
        del turma[nome]  # Apaga o aluno do dicionário
        print("Aluno removido.")
    else:
        print("Aluno não encontrado.")


def editar_nome():
    """
    Altera o nome de um aluno existente.
    """
    nome_antigo = pedir_nome()

    if nome_antigo not in turma:
        print("Aluno não encontrado.")
        return

    nome_novo = pedir_nome()

    # Mantém os dados, mas muda o nome (chave do dicionário)
    turma[nome_novo] = turma.pop(nome_antigo)
    print("Nome do aluno atualizado.")


def procurar_aluno():
    """
    Mostra os dados de um aluno específico.
    """
    nome = pedir_nome()

    if nome in turma:
        dados = turma[nome]
        print(f"""
Aluno: {nome}
Faltas: {dados['faltas']}
Falta de material: {dados['material']}
Falta disciplinar: {dados['disciplinar']}
        """)
    else:
        print("Aluno não encontrado.")


def listar_alunos():
    """
    Lista todos os alunos registados.
    """
    if not turma:  # Se o dicionário estiver vazio
        print("Não há alunos registados.")
        return

    for nome, dados in turma.items():
        print(f"""
Aluno: {nome}
  Faltas: {dados['faltas']}
  Material: {dados['material']}
  Disciplinar: {dados['disciplinar']}
        """)


# ==================================================
#                REGISTOS
# ==================================================

def marcar_falta():
    """
    Regista uma falta normal.
    """
    nome = pedir_nome()

    if nome in turma:
        turma[nome]["faltas"] += 1  # Soma uma falta
        print("Falta registada.")
    else:
        print("Aluno não encontrado.")


def falta_material():
    """
    Regista uma falta de material.
    """
    nome = pedir_nome()

    if nome in turma:
        turma[nome]["material"] += 1
        print("Falta de material registada.")
    else:
        print("Aluno não encontrado.")


def falta_disciplinar():
    """
    Regista uma falta disciplinar.
    """
    nome = pedir_nome()

    if nome in turma:
        turma[nome]["disciplinar"] += 1
        print("Falta disciplinar registada.")
    else:
        print("Aluno não encontrado.")


def limpar_registos():
    """
    Coloca todos os registos de um aluno a zero.
    """
    nome = pedir_nome()

    if nome in turma:
        turma[nome] = {
            "faltas": 0,
            "material": 0,
            "disciplinar": 0
        }
        print("Registos limpos.")
    else:
        print("Aluno não encontrado.")


# ==================================================
#                ESTATÍSTICAS
# ==================================================

def estatisticas():
    """
    Mostra estatísticas gerais da turma.
    """
    if not turma:
        print("Não há alunos.")
        return

    # Soma todas as faltas de todos os alunos
    total_faltas = sum(a["faltas"] for a in turma.values())
    total_material = sum(a["material"] for a in turma.values())
    total_disciplinar = sum(a["disciplinar"] for a in turma.values())

    print(f"""
--- ESTATÍSTICAS ---
Total de alunos: {len(turma)}
Total de faltas: {total_faltas}
Total faltas de material: {total_material}
Total faltas disciplinares: {total_disciplinar}
    """)


def avisos():
    """
    Mostra alunos com 5 ou mais faltas.
    """
    print("\n--- ALUNOS COM MUITAS FALTAS ---")

    for nome, dados in turma.items():
        if dados["faltas"] >= 5:
            print(f"{nome} - {dados['faltas']} faltas")


# ==================================================
#                    MENU
# ==================================================

def main():
    """
    Função principal do programa.
    Controla o menu e as opções.
    """
    carregar_dados()  # Carrega os dados ao iniciar o programa

    while True:
        print("""
--- GESTOR DE TURMA ---
1  - Adicionar aluno
2  - Remover aluno
3  - Listar alunos
4  - Procurar aluno
5  - Editar nome do aluno
6  - Marcar falta
7  - Falta de material
8  - Falta disciplinar
9  - Limpar registos do aluno
10 - Estatísticas da turma
11 - Avisos de faltas
12 - Guardar dados
0  - Sair
        """)

        opcao = input("Escolha uma opção: ")

        # Estrutura de decisão para o menu
        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            remover_aluno()
        elif opcao == "3":
            listar_alunos()
        elif opcao == "4":
            procurar_aluno()
        elif opcao == "5":
            editar_nome()
        elif opcao == "6":
            marcar_falta()
        elif opcao == "7":
            falta_material()
        elif opcao == "8":
            falta_disciplinar()
        elif opcao == "9":
            limpar_registos()
        elif opcao == "10":
            estatisticas()
        elif opcao == "11":
            avisos()
        elif opcao == "12":
            guardar_dados()
        elif opcao == "0":
            guardar_dados()
            print("A sair do programa...")
            break
        else:
            print("Opção inválida!")


# --------------------------------------------------
# Ponto de entrada do programa
# Só executa o main se este ficheiro for o principal
# --------------------------------------------------
if __name__ == "__main__":
    main()
