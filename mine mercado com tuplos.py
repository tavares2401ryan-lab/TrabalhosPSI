# ==========================================
# MINI PROJETO 1 - SISTEMA DE GESTÃO DE LOJA
# ==========================================

# Estrutura do Produto:
# (id, nome, preco, quantidade, categoria)

# Produtos já cadastrados
produtos = [
    (1, "Arroz", 1.99, 50, "Alimentacao"),
    (2, "Leite", 0.89, 30, "Laticinios"),
    (3, "Detergente", 2.49, 20, "Limpeza"),
    (4, "Pao", 0.25, 100, "Padaria"),
    (5, "Cafe", 3.99, 15, "Bebidas"),
    (6, "Acucar", 1.20, 40, "Alimentacao"),
    (7, "Champo", 4.50, 18, "Higiene"),
    (8, "Massa", 1.10, 60, "Alimentacao"),
    (9, "Sumo", 1.75, 25, "Bebidas"),
    (10, "Sabonete", 0.99, 35, "Higiene")
]

contador_id = 11


# ------------------------------------------
# Funções Utilitárias
# ------------------------------------------

def gerar_id():
    global contador_id
    novo_id = contador_id
    contador_id += 1
    return novo_id


def validar_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto.replace(" ", "").isalpha():
            return texto
        else:
            print("⚠ Apenas letras são permitidas.")


def validar_int(mensagem):
    while True:
        valor = input(mensagem)
        if valor.isdigit():
            return int(valor)
        else:
            print("⚠ Digite apenas números inteiros.")


def validar_float(mensagem):
    while True:
        valor = input(mensagem).replace(",", ".")
        if valor.replace(".", "", 1).isdigit():
            return float(valor)
        else:
            print("⚠ Digite um número válido.")


def procurar_por_id(id_produto):
    for produto in produtos:
        if produto[0] == id_produto:
            return produto
    return None


# ------------------------------------------
# Mostrar Produtos
# ------------------------------------------

def listar_produtos():
    print("\n=== LISTA DE PRODUTOS ===")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print(f"{'ID':<5}{'Nome':<15}{'Preço':<10}{'Qtd':<8}{'Categoria'}")
    print("-" * 55)

    for p in produtos:
        print(f"{p[0]:<5}{p[1]:<15}€{p[2]:<9.2f}{p[3]:<8}{p[4]}")

    print("-" * 55)


# ------------------------------------------
# CRUD
# ------------------------------------------

def adicionar_produto():
    print("\n=== ADICIONAR PRODUTO ===")

    nome = validar_texto("Nome do produto: ")
    preco = validar_float("Preço (€): ")
    quantidade = validar_int("Quantidade: ")
    categoria = validar_texto("Categoria: ")

    produto = (gerar_id(), nome, preco, quantidade, categoria)
    produtos.append(produto)

    print("✅ Produto adicionado com sucesso!")
    listar_produtos()


def atualizar_produto():
    print("\n=== ATUALIZAR PRODUTO ===")
    id_produto = validar_int("ID do produto: ")

    produto = procurar_por_id(id_produto)

    if not produto:
        print("❌ Produto não encontrado.")
        return

    nome = validar_texto("Novo nome: ")
    preco = validar_float("Novo preço: ")
    quantidade = validar_int("Nova quantidade: ")
    categoria = validar_texto("Nova categoria: ")

    produtos.remove(produto)
    produtos.append((id_produto, nome, preco, quantidade, categoria))

    print("✅ Produto atualizado com sucesso!")
    listar_produtos()


def remover_produto():
    print("\n=== REMOVER PRODUTO ===")
    id_produto = validar_int("ID do produto: ")

    produto = procurar_por_id(id_produto)

    if not produto:
        print("❌ Produto não encontrado.")
        return

    produtos.remove(produto)
    print("✅ Produto removido com sucesso!")
    listar_produtos()


# ------------------------------------------
# Menu Principal
# ------------------------------------------

def menu():

    print("\n📦 PRODUTOS DISPONÍVEIS NA LOJA:")
    listar_produtos()

    while True:
        print("\n" + "=" * 40)
        print("      SISTEMA DE GESTÃO DE LOJA")
        print("=" * 40)
        print("1 - Adicionar Produto")
        print("2 - Mostrar Produtos")
        print("3 - Atualizar Produto")
        print("4 - Remover Produto")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            remover_produto()
        elif opcao == "0":
            print("Encerrando sistema...")
            break
        else:
            print("❌ Opção inválida.")


menu()