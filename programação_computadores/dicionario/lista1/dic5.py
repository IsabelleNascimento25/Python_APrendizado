# Crie um programa que receba os dados de vários produtos de um estoque.
# Para cada produto, armazene em um dicionário o nome como chave e a
# quantidade como valor. Depois:
# a. exiba todos os produtos com estoque igual a zero;
# b. exiba a soma total de itens em estoque.
# Execução simulada:
# Entrada:
# Quantos produtos deseja cadastrar? 3
# Nome do produto: arroz
# Quantidade: 0
# Nome do produto: feijão
# Quantidade: 5
# Nome do produto: macarrão
# Quantidade: 2
# Saída:
# Produtos com estoque zerado:
# arroz
# Total de itens em estoque: 7

estoque = {}

qtd = int(input('Quantos produtos deseja cadastrar? '))

for i in range(qtd):
    nome = input('Nome do produto: ').lower()
    quantidade = int(input('Quantidade: '))
    
    estoque[nome] = quantidade

print('\nProdutos com estoque zerado:')
for produto in estoque:
    if estoque[produto] == 0:
        print(produto)

total = 0
for produto in estoque:
    total += estoque[produto]

print('Total de itens em estoque:', total)