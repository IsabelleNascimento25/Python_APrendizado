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