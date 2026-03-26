# Desafio 1: O Filtro de Pares
# Neste, você vai usar o range para pedir números
# , mas só vai dar o append na lista se o número for par.

# Tarefa: Peça para o usuário digitar 6 números.

# Ação: Guarde em uma lista apenas os que forem pares.

# Resultado: No final, mostre a lista e quantos números foram guardados (use len(lista)).





numpar = []

for i in range(6):
    n = int(input('Digite um n: '))
    if n % 2==0:
     numpar.append(n)  # Esta linha precisa estar alinhada aqui dentro
    print (numpar)




    # Conte quantos números o usuário digitou até digitar 0

    