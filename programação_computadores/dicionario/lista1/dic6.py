alunos = {}

qtd = int(input('Quantos alunos deseja cadastrar? '))

for i in range(qtd):
    nome = input('Nome do aluno: ')
    nota = float(input('Nota: '))
    
    alunos[nome] = nota

resultado = {}

for nome in alunos:
    if alunos[nome] >= 6:
        resultado[nome] = 'aprovado'
    else:
        resultado[nome] = 'reprovado'

print(resultado)