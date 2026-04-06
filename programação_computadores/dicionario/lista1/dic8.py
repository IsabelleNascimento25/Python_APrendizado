# Crie um programa que receba uma palavra e monte um dicionário em que:
# a. a chave seja cada letra diferente da palavra;
# b. o valor seja a posição da primeira vez em que essa letra aparece.
# Execução simulada:
# Entrada:
# banana
# Saída:
# {'b': 0, 'a': 1, 'n': 2}

palavra = input('Digite uma palavra: ')

dicionario = {}

for i in range(len(palavra)):
    letra = palavra[i]
    
    if letra not in dicionario:
        dicionario[letra] = i

print(dicionario)