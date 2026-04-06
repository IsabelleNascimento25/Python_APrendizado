
dicionario = {}

while True:
    chave = input("Digite a palavra em português (ou 'sair'): ").lower()
    
    if chave == 'sair':
        break
    
    valor = input("Digite a tradução em inglês: ").lower()
    
    dicionario[chave] = valor
    print("Adicionado com sucesso!\n")

print("\nDicionário final:")
print(dicionario)