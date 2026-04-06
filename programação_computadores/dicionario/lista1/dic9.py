# Crie um programa que armazene em um dicionário os nomes de vendedores
# e o total de vendas de cada um. Depois, o programa deve exibir:
# a. o nome do vendedor com maior total de vendas;
# b. quantos vendedores venderam mais de 1000.
# Execução simulada:
# Entrada:
# Nome: Ana
# Vendas: 1200
# Nome: João
# Vendas: 800
# Nome: Maria



vendedores = {}

qtd = int(input('Quantos vendedores deseja cadastrar? '))

for i in range(qtd):
    nome = input('Nome: ')
    vendas = float(input('Vendas: '))
    
    vendedores[nome] = vendas

# descobrir o maior
maior_nome = ''
maior_venda = 0

for nome in vendedores:
    if vendedores[nome] > maior_venda:
        maior_venda = vendedores[nome]
        maior_nome = nome

# contar quantos venderam mais de 1000
contador = 0

for nome in vendedores:
    if vendedores[nome] > 1000:
        contador += 1

print('Maior vendedor:', maior_nome)
print('Quantidade que vendeu mais de 1000:', contador)