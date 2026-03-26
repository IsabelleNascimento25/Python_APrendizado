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