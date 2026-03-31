#  Use conjuntos (set) como estrutura principal.
# − Utilize: entrada = input().split() para ler vários valores na mesma
# linha. A variável entrada vai ser uma lista (list).
# 1) Leia duas linhas com inteiros separados por espaço e mostre o conjunto dos
# números que aparecem somente na primeira linha e o conjunto dos números
# que aparecem somente na segunda linha.
# Entrada (exemplo):
# 1 2 3 4
# 3 4 5 6
# Saída (exemplo):
# Só na primeira: {1, 2}
# Só na segunda: {5, 6}
linha1 = set(input().split())
linha2 = set(input().split())

so1 = linha1 - linha2
so2 = linha2 - linha1

print("Só na primeira:", so1)
print("Só na segunda:", so2)

#  Leia três linhas com nomes de alunos que participaram de três atividades e
# mostre o conjunto dos alunos que participaram de exatamente duas
# atividades.
# Entrada (exemplo):
# Ana João Maria
# Maria Pedro Ana
# Ana Carlos Pedro
# Saída (exemplo):
# Duas atividades: {Maria, Pedro}

linha1 = set("Ana João Maria".split())
linha2 = set("Maria Pedro Ana".split())
linha3 = set("Ana Carlos Pedro".split())

duas = (linha1 & linha2) | (linha1 & linha3) | (linha2 & linha3)
tres = linha1 & linha2 & linha3

resultado = duas - tres

print("Duas atividades:", resultado)

#  Leia uma linha com inteiros separados por espaço e separe os números em
# dois conjuntos: pares e ímpares.
# Entrada (exemplo):
# 1 2 3 4 5 6
# Saída (exemplo):
# Pares: {2, 4, 6}
# Ímpares: {1, 3, 5}

numeros = set("1 2 3 4 5 6".split())

pares = set()
impares = set()

for n in numeros:
    n = int(n)
    if n % 2 == 0:
        pares.add(n)
    else:
        impares.add(n)

print("Pares:", pares)
print("Ímpares:", impares)

# Leia uma linha com palavras e mostre o conjunto das palavras que têm
# tamanho maior que 4.
# Entrada (exemplo):
# dados python ia casa computador
# Saída (exemplo):
# Maiores que 4: {dados, python, computador}

palavras = set("dados python ia casa computador".split())

maiores = set()

for p in palavras:
    if len(p) > 4:
        maiores.add(p)

print("Maiores que 4:", maiores)

# Leia duas linhas com nomes de alunos: a primeira contém os matriculados e
# a segunda contém os que fizeram a prova. Mostre o conjunto dos alunos que
# fizeram a prova sem estar matriculados e o conjunto dos matriculados que
# não fizeram a prova.
# Entrada (exemplo):
# Ana João Maria
# João Pedro
# Saída (exemplo):
# Irregulares: {Pedro}
# Ausentes: {Ana, Maria}

matriculados = set("Ana João Maria".split())
prova = set("João Pedro".split())

irregulares = prova - matriculados
ausentes = matriculados - prova

print("Irregulares:", irregulares)
print("Ausentes:", ausentes)

#  Leia uma linha com números inteiros e mostre o menor valor distinto e o
# maior valor distinto.
# Entrada (exemplo):
# 5 2 2 9 1 5
# Saída (exemplo):
# Menor: 1
# Maior: 9
numeros = set(map(int, "5 2 2 9 1 5".split()))

print("Menor:", min(numeros))
print("Maior:", max(numeros))

# Leia uma linha com nomes de usuários bloqueados. Depois leia nomes de
# usuários tentando entrar até digitar "fim". Mostre o conjunto dos usuários que
# tentaram entrar e não estavam bloqueados.
# Entrada (exemplo):
# ana joao
# pedro
# joao
# maria
# fim
# Saída (exemplo):
# Liberados: {pedro, maria}

bloqueados = set("ana joao".split())

tentativas = set()

while True:
    nome = input()
    if nome == "fim":
        break
    tentativas.add(nome)

liberados = tentativas - bloqueados

print("Liberados:", liberados)

#  Leia uma linha com inteiros e mostre o conjunto dos números que aparecem
# mais de uma vez.
# Entrada (exemplo):
# 1 2 3 2 4 5 1
# Saída (exemplo):
Repetidos: {1, 2}
entrada = "1 2 3 2 4 5 1".split()

vistos = set()
repetidos = set()

for n in entrada:
    if n in vistos:
        repetidos.add(int(n))
    else:
        vistos.add(n)

print("Repetidos:", repetidos)

# )Leia duas linhas com inteiros e mostre o conjunto dos números da primeira
# linha que não aparecem na segunda e que são pares.
# Entrada (exemplo):
# 1 2 3 4 6
# 3 5 7
# Saída (exemplo):
# Resultado: {2, 4, 6}

linha1 = set("1 2 3 4 6".split())
linha2 = set("3 5 7".split())

resultado = set()

for n in linha1:
    n = int(n)
    if n % 2 == 0 and str(n) not in linha2:
        resultado.add(n)

print("Resultado:", resultado)