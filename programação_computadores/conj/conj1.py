# =============================================
# Programa: Contar valores distintos usando conjunto (set)
# =============================================

# Passo 1: Definimos os números diretamente no código
# (não precisa digitar nada quando rodar)
numeros_texto = ("5 2 2 3 5 7 7 7")

# Passo 2: Separamos os números usando split()
# Isso transforma a string em uma lista de strings
entrada = numeros_texto.split()

# Passo 3: Convertemos cada string para número inteiro (int)
numeros = [int(x) for x in entrada]

# Passo 4: Criamos um conjunto (set)
# O set remove automaticamente todos os números repetidos
distintos = set(numeros)

# Passo 5: Contamos quantos números diferentes existem
quantidade = len(distintos)

# Passo 6: Mostramos o resultado final
print(f"Quantidade de distintos: {quantidade}")