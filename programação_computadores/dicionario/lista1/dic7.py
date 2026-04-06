# Crie um programa que tenha dois dicionários:
# a. o primeiro relaciona códigos de produtos aos nomes;
# b. o segundo relaciona os mesmos códigos aos preços.
# Ao final, o programa deve pedir um código e exibir o nome e o preço do
# produto correspondente. Se o código não existir, exiba "Código inválido".
# Execução simulada:
# Entrada:
# Digite o código do produto: 1
# Saída:
# Produto:
# Caderno
# Preço: 18.5
# 8) Crie um pro

codigos_nomes = {}
codigos_precos = {}

qtd = int(input('Quantos produtos deseja cadastrar? '))

for i in range(qtd):
    codigo = int(input('Digite o código do produto: '))
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço: '))
    
    codigos_nomes[codigo] = nome
    codigos_precos[codigo] = preco

busca = int(input('\nDigite o código do produto: '))

if busca in codigos_nomes:
    print('Produto:')
    print(codigos_nomes[busca])
    print('Preço:', codigos_precos[busca])
else:
    print('Código inválido')