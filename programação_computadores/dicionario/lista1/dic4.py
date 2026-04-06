# Crie um dicionário que relacione países e suas capitais. O programa deve
# solicitar ao usuário o nome de um país e verificar se ele está presente no
# dicionário. Se estiver, exiba a capital correspondente. Caso contrário, exiba
# "País não encontrado".
# Exemplos de execução:
# Entrada: Brasil → Saída: A capital de Brasil é Brasília
# Entrada: França → Saída: A capital de França é Paris
# Entrada: Argentina → Saída: País não encontrado

entrada = input('Digite um desses paises: (Brasil), (França), (Argentina) ')

paises ={
    'Brasil' : 'A capital de Brasil é Brasília',
    'França' : 'A capital de França é Paris',
    'Argentina' : 'A capital da Argentina é Buenos Aires'
}

if entrada in paises:
    print(paises[entrada])
else:
    print('Pais não detectado')
