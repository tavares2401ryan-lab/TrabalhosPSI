# ===============================
# GESTOR DE TURMA (SEM IMPORTS)
# ===============================

turma = {}


# ===============================
# UTILIDADES
# ===============================

def pedir_nome():
    while True:
        nome = input("Nome do aluno: ").strip()
        if nome.replace(" ", "").isalpha():
            return nome.title()
        print("Erro: nome inválido.")


def aluno_existe(nome):
    return nome in turma


def mostrar_aluno(nome):
    a = turma[nome]
    print(f"""
Aluno: {nome}
Faltas: {a['faltas']}
Material: {a['material']}
Disciplinar: {a['disciplinar']}
""")


# ===============================
# ALUNOS
# ===============================

def adicionar_aluno():
    nome = pedir_nome()
    if aluno_existe(nome):
        print("Aluno já existe.")
        return

    turma[nome] = {
        "faltas": 0,
        "material": 0,
        "disciplinar": 0
    }
    print("Aluno adicionado.")


def remover_aluno():
    nome = pedir_nome()
    if aluno_existe(nome):
        del turma[nome]
        print("Aluno removido.")
    else:
        print("Aluno não encontrado.")


def editar_nome():
    nome_antigo = pedir_nome()
    if not aluno_existe(nome_antigo):
        print("Aluno não encontrado.")
        return

    nome_novo = pedir_nome()
    turma[nome_novo] = turma.pop(nome_antigo)
    print("Nome alterado.")


def listar_alunos():
    if not turma:
        print("Não há alunos registados.")
        return

    for nome in turma:
        mostrar_aluno(nome)


def procurar_aluno():
    nome = pedir_nome()
    if aluno_existe(nome):
        mostrar_aluno(nome)
    else:
        print("Aluno não encontrado.")


# ===============================
# REGISTOS
# ===============================

def registar_falta(chave, texto):
    nome = pedir_nome()
    if aluno_existe(nome):
        turma[nome][chave] += 1
        print(texto)
    else:
        print("Aluno não encontrado.")


def limpar_registos():
    nome = pedir_nome()
    if aluno_existe(nome):
        for k in turma[nome]:
            turma[nome][k] = 0
        print("Registos limpos.")
    else:
        print("Aluno não encontrado.")


# ===============================
# ESTATÍSTICAS / AVISOS
# ===============================

def estatisticas():
    if not turma:
        print("Não há alunos.")
        return

    total_faltas = 0
    total_material = 0
    total_disciplinar = 0

    for a in turma.values():
        total_faltas += a["faltas"]
        total_material += a["material"]
        total_disciplinar += a["disciplinar"]

    print(f"""
--- ESTATÍSTICAS ---
Total de alunos: {len(turma)}
Total de faltas: {total_faltas}
Faltas de material: {total_material}
Faltas disciplinares: {total_disciplinar}
""")


def avisos():
    print("\n--- AVISO DE FALTAS ---")
    encontrou = False

    for nome, a in turma.items():
        if a["faltas"] >= 5:
            print(f"{nome} - {a['faltas']} faltas")
            encontrou = True

    if not encontrou:
        print("Nenhum aluno com faltas excessivas.")


# ===============================
# MENU
# ===============================

def main():
    while True:
        print("""
--- GESTOR DE TURMA ---
1  Adicionar aluno
2  Remover aluno
3  Editar nome
4  Listar alunos
5  Procurar aluno
6  Marcar falta
7  Falta de material
8  Falta disciplinar
9  Limpar registos
10 Estatísticas
11 Avisos
0  Sair
""")

        op = input("Opção: ")

        if op == "1":
            adicionar_aluno()
        elif op == "2":
            remover_aluno()
        elif op == "3":
            editar_nome()
        elif op == "4":
            listar_alunos()
        elif op == "5":
            procurar_aluno()
        elif op == "6":
            registar_falta("faltas", "Falta registada.")
        elif op == "7":
            registar_falta("material", "Falta de material registada.")
        elif op == "8":
            registar_falta("disciplinar", "Falta disciplinar registada.")
        elif op == "9":
            limpar_registos()
        elif op == "10":
            estatisticas()
        elif op == "11":
            avisos()
        elif op == "0":
            print("A sair do programa...")
            break
        else:
            print("Opção inválida.")


main()
