while True:
    try:
        quantidade = int(input("Quantas notas quer inserir? "))
        if quantidade <= 0:
            print("Erro: a quantidade deve ser maior que zero.")
        else:
            break
    except ValueError:
        print("Erro: digite apenas números inteiros.")

notas = []

for i in range(quantidade):
    while True:
        try:
            nota = float(input(f"Digite a nota {i + 1}: "))
            notas.append(nota)
            break
        except ValueError:
            print("Erro: digite um número válido para a nota.")

print("\n--- Resultados ---")
print("Todas as notas:", notas)
print("Nota mais alta:", max(notas))
print("Nota mais baixa:", min(notas))
print("Média das notas:", sum(notas) / len(notas))
