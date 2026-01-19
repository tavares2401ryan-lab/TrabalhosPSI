# GERADOR DE PALAVRA-PASSE
# ============================

print("GERADOR DE PALAVRA-PASSE SEGURA\n")

nome = input("Digite o seu nome: ")
ano = input("Digite o seu ano de nascimento: ")
frase = input("Digite uma frase: ")

# Garantir que o ano só tem números
while ano.isdigit() == False:
    print("Erro: use apenas números.")
    ano = input("Digite o seu ano de nascimento: ")

# -------- GERAR SIGLA --------
sigla = ""
nova_palavra = True

for letra in frase:
    if nova_palavra == True and letra.isalpha():
        sigla = sigla + letra.upper()
        nova_palavra = False

    if letra == " ":
        nova_palavra = True

# -------- MONTAR PASSWORD --------
password = ""
contador = 0

for letra in nome:
    if letra.isalpha():
        if contador % 2 == 0:
            password = password + letra.upper()
        else:
            password = password + letra.lower()
        contador = contador + 1

# Adiciona sigla
password = password + sigla

# Adiciona números do ano (invertidos)
for numero in ano:
    if numero.isdigit():
        password = password + numero

print("\nPalavra-passe gerada:", password)
