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