# Sistema de Gestão de Participantes de Evento Escolar
from Menudoevento import menu
# Tuplo com informações do evento
evento = ("Feira Escolar", "10/04/2026", "Parque Aquatico")

# Lista de participantes
participantes = []

# Set para emails únicos
emails_registrados = set()


def mostrar_evento():
    print("\n===== INFORMAÇÕES DO EVENTO =====")
    print("Evento:", evento[0])
    print("Data:", evento[1])
    print("Local:", evento[2])


def adicionar_participante():
    print("\n--- Adicionar Participante ---")

    nome = input("Nome: ")
    if nome.strip() == "":
        print("❌ Nome inválido.")
        return

    idade = input("Idade: ")
    if not idade.isdigit():
        print("❌ Idade deve ser um número.")
        return

    email = input("Email: ")
    if "@" not in email:
        print("❌ Email inválido.")
        return

    turma = input("Turma (ex: 8A): ")
    if len(turma) < 2:
        print("❌ Turma inválida.")
        return

    if email in emails_registrados:
        print("❌ Este email já foi registrado.")
        return

    participante = (nome, idade, email, turma)

    participantes.append(participante)
    emails_registrados.add(email)

    print("✅ Participante adicionado corretamente!")

def ver_participantes():
    print("\n--- Lista de Participantes ---")

    if len(participantes) == 0:
        print("Nenhum participante registrado.")
        return

    for i, p in enumerate(participantes, start=1):
        print(f"{i}. Nome: {p[0]} | Idade: {p[1]} | Email: {p[2]} | Turma: {p[3]}")


def alterar_turma():
    print("\n--- Alterar Turma ---")
    email = input("Email do participante: ")

    for i, p in enumerate(participantes):
        if p[2] == email:
            nova_turma = input("Nova turma: ")

            # recriar tuplo (tuplos não podem ser alterados)
            participante_novo = (p[0], p[1], p[2], nova_turma)

            participantes[i] = participante_novo

            print("✅ Turma alterada com sucesso!")
            return

    print("❌ Participante não encontrado.")


def remover_participante():
    print("\n--- Remover Participante ---")
    email = input("Email do participante: ")

    for p in participantes:
        if p[2] == email:
            participantes.remove(p)
            emails_registrados.remove(email)
            print("✅ Participante removido.")
            return

    print("❌ Participante não encontrado.")


def estatisticas():
    print("\n--- Estatísticas ---")
    print("Total de participantes:", len(participantes))
    print("Emails únicos:", len(emails_registrados))


