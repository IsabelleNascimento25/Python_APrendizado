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
