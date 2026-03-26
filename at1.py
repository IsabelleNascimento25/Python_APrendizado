# SUPER BÁSICO

# (Entender repetição)

# Mostre números de 1 a 10 com for
n = 0
for n in range(1,11):
    print (n)

# Mostre números de 1 a 10 com while
n2= 1
while n2 <= 10:
    print (n2)
    n2 +=1
# Mostre números de 10 até 1
n3= 10
while n3 >= 1:
    print (n3)
    n3-=1
# Mostre apenas números pares de 1 a 20

n4 = 2
while n4 <=20:
    if n4 % 2 ==0 :
        print (n4)
    n4 +=2
# Mostre apenas números ímpares de 1 a 20

# 🟡 NÍVEL 2 — CONTROLE SIMPLES
# Mostre a soma dos números de 1 a 10
n6 = 1
soma = 0
while n6 <= 10:
    soma + n6
    n6+= 1

print (n6)
# Mostre a soma dos números de 1 a N (digitado pelo usuário)
nu1 = int(input('Início: '))
nu2 = int(input('Fim: '))

total_soma = 0 

while nu1 <= nu2:
    total_soma += nu1  # Acumula o valor atual de nu1 na soma
    nu1 += 1           # Faz o nu1 "caminhar" (ex: 1 -> 2 -> 3...)

print(f"A soma de todos os números é: {total_soma}")2

# Mostre a média de 5 números digitados
numeros = [] # Criamos uma lista vazia
for i in range(5):
    n = float(input('Digite um n: '))
    numeros.append(n) # Adiciona o número na lista

# Agora sim, sum() e len() funcionam!
media = sum(numeros) / len(numeros)
print(f"A média é: {media}")

# Conte quantos números o usuário digitou até digitar 0
# Conte quantos números o usuário digitou até digitar 0
contador = 0
n = int(input('digite um n: '))
while n != 0:
   n= int(input('digite outro: '))
# Some números até o usuário digitar 0

# 🟠 NÍVEL 3 — CONDIÇÃO + LOOP
# Mostre quantos números pares existem entre 1 e 50
n8 = 0
for n8 in range(1,50):
    resu = n8 %2 ==0
    print(resu)


# Mostre quantos números ímpares existem entre 1 e 50
# Leia 10 números e mostre quantos são positivos
# Leia 10 números e mostre quantos são negativos
# Leia 10 números e mostre o maior número
# 🔵 NÍVEL 4 — TABUADA
# Mostre a tabuada de um número
# Mostre todas as tabuadas de 1 a 10
# Mostre a tabuada só dos números pares
# Mostre a tabuada invertida (10 até 1)
# Peça um número e mostre até qual multiplicação (ex: até 5)
# 🟣 NÍVEL 5 — ACUMULADORES
# Some apenas números pares digitados pelo usuário
# Some apenas números ímpares
# Leia números até 0 e mostre:
# soma
# quantidade
# média
# Leia 10 números e mostre o menor
# Leia 10 números e mostre maior e menor