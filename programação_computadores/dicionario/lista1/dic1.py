# Crie um dicionário que contenha algumas palavras em português como
# chaves e suas respectivas traduções em inglês como valores. O programa
# deve solicitar ao usuário que digite uma palavra em português e exibir sua
# tradução em inglês. Se a palavra não estiver no dicionário, deve ser exibida a
# mensagem "Não encontrada".
# Exemplos de execução:
# Entrada: gato → Saída: cat
# Entrada: casa → Saída: house
# Entrada: livro → Saída: Não encontrada

palavra = input('Digite uma dessas 3 palavras: gato, casa ou livro: ')

dicionario = {
     'gato': 'cat',
    'casa': 'house',
    'livro': 'book'
}

if palavra in dicionario:
    print(dicionario[palavra])
else: 
    print('Palavra não encontrada')
