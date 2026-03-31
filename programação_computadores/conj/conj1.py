# =============================================
# Programa: Contar valores distintos usando conjunto (set)
# =============================================

# Passo 1: Definimos os números diretamente no código
# (não precisa digitar nada quando rodar)
numeros_texto = ("5 2 2 3 5 7 7 7")

# Passo 2: Separamos os números usando split()
# Isso transforma a string em uma lista de strings
entrada = numeros_texto.split()

# Passo 3: Convertemos cada string para número inteiro (int)
numeros = [int(x) for x in entrada]

# Passo 4: Criamos um conjunto (set)
# O set remove automaticamente todos os números repetidos
distintos = set(numeros)

# Passo 5: Contamos quantos números diferentes existem
quantidade = len(distintos)

# Passo 6: Mostramos o resultado final
print(f"Quantidade de distintos: {quantidade}")


# =============================================
# União de nomes das duas turmas usando set
# =============================================

# Definimos os nomes das turmas (corrigido)
turmaA = "Ana João Maria"
turmaB = "João Pedro"

# Convertemos as strings em conjuntos (sets)
# split() separa os nomes pelo espaço
setA = set(turmaA.split())
setB = set(turmaB.split())

# Faz a união dos dois conjuntos
UniaoTotal = setA.union(setB)

# Mostra o resultado no formato pedido
print(f"União: {UniaoTotal}")
print(f"Total: {len(UniaoTotal)}")

#  Leia duas linhas com palavras-chave e exiba o conjunto com as palavras que
# aparecem em ambas as linhas (se não houver, mostre o conjunto vazio).
# Entrada (exemplo):
# Linha 1: dados ciência python limpeza
# Linha 2: estatística python dados regressão
# Saída (exemplo):
# Comuns: {python, dados}

linha1 = "dados ciência python limpeza"
linha2 = "estatística python dados regressão"

setA = set(linha1.split())
setB = set(linha2.split())

comum = (setA.intersection(setB))  

print (f'comuns: {comum}')


#  Leia duas linhas: a primeira com os códigos cadastrados e a segunda com os
# códigos presentes; exiba o conjunto com os cadastrados que não aparecem
# na lista de presentes.
# Entrada (exemplo):
# Cadastrados: A1 A2 A3 A4
# Presentes: A2 A4
# Saída (exemplo):
# Faltantes: {A1, A3}

Cadastrados =  'A1 A2 A3 A4'
Presentes =     'A2 A4'

setcadastrados = set(Cadastrados.split())
setpresentes = set(Presentes.split())

diferenca = (setcadastrados.difference(setpresentes))
 
print (diferenca)

#  Leia duas linhas: a primeira contém os nomes presentes no momento “antes”
# e a segunda contém os nomes presentes no momento “depois”. Exiba o
# conjunto das pessoas que aparecem em exatamente uma das duas linhas —
# isto é, quem saiu (estava antes e não está depois) ou entrou (não estava
# antes e está depois). Ignore duplicatas em cada linha; a ordem do conjunto
# exibido é arbitrária.
# Entrada (exemplo):
# Antes: Ana João Maria
# Depois: Ana Pedro Maria Luísa
# Saída (exemplo):
# Mudanças: {João, Pedro, Luísa}

Antes = 'Ana João Maria'
Depois = 'Ana Pedro Maria Luísa'

setantes = set(Antes.split())
setdepois =set(Depois.split())

mudanca =(setantes.symmetric_difference(setdepois))

print (f'mudança= {mudanca}')

# Leia uma linha com e-mails autorizados e, na linha seguinte, um e-mail de
# usuário; exiba “Acesso liberado” se o e-mail informado estiver na lista de
# autorizados, ou “Acesso negado” caso contrário.
# Entrada (exemplo):
# Autorizados: ana@ex.com joao@ex.com maria@ex.com
# Usuário: joao@ex.com
# Saída (exemplo):
# Acesso liberado

Autorizados = {'ana@ex.com', 'joao@ex.com', 'maria@ex.com'}
usuario = int(input('Digite seu usuário: '))

if usuario in Autorizados:
    print ('Acesso liberado')
else:
    print('Acesso Negado')

    #  Leia uma linha com e-mails separados por espaço, desconsidere diferenças
# entre maiúsculas e minúsculas, extraia a parte após “@” e mostre o conjunto
# de domínios distintos e, na linha seguinte, a quantidade total de domínios.
# Entrada (exemplo):
# Ana@Ex.com JOAO@ex.com maria@uni.br pedro@uni.br
# Saída (exemplo):
# Domínios: {ex.com, uni.br}
# Total: 2

entrada = "Ana@Ex.com JOAO@ex.com maria@uni.br pedro@uni.br".split()

dominios = set()

for email in entrada:
    email = email.lower()
    dominio = email.split("@")[1]
    dominios.add(dominio)

print("Domínios:", dominios)
print("Total:", len(dominios))

# Leia uma linha com itens (strings), forme um conjunto e imprima um item por
# linha, removendo um elemento do conjunto a cada impressão até esvaziá-lo;
# ao final, imprima “Vazio”. A ordem de impressão pode variar.
# Entrada (exemplo):
# maçã banana pera
# Saída (exemplo):
# banana
# maçã
# pera
# Vazio
# (a ordem pode variar)

entrada = "maçã banana pera".split()

itens = set(entrada)

while itens:
    print(itens.pop())

print("Vazio")

#  Leia três linhas com códigos de quem entregou cada uma das três listas;
# exiba o conjunto de quem aparece em pelo menos uma das linhas e, em
# outra linha, o conjunto de quem aparece nas três linhas.
# Entrada (exemplo):
# lista1: A1 A2 A3
# lista2: A2 A4
# lista3: A2 A3 A5
# Saída (exemplo):
# Pelo menos uma: {A1, A2, A3, A4, A5}
# Todas: {A2}
l1 = set("A1 A2 A3".split())
l2 = set("A2 A4".split())
l3 = set("A2 A3 A5".split())

pelo_menos_uma = l1 | l2 | l3
todas = l1 & l2 & l3

print("Pelo menos uma:", pelo_menos_uma)
print("Todas:", todas)

# Leia uma linha com os itens disponíveis no estoque e outra com os itens
# pedidos (podem conter repetidos); mostre o conjunto de itens que podem ser
# atendidos (presentes nas duas linhas) e, em seguida, o conjunto de itens
# pedidos que não estão disponíveis.
# Entrada (exemplo):
# Estoque: teclado mouse monitor
# Pedidos: mouse mouse teclado webcam
# Saída (exemplo):
# Atendidos: {mouse, teclado}
# Indisponíveis: {webcam}

estoque = set("teclado mouse monitor".split())
pedidos = set("mouse mouse teclado webcam".split())

atendidos = estoque & pedidos
indisponiveis = pedidos - estoque

print("Atendidos:", atendidos)
print("Indisponíveis:", indisponiveis)