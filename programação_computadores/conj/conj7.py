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


