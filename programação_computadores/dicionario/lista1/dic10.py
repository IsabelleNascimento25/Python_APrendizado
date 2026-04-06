
# )Crie um programa que cadastre nomes de alunos e suas notas em um
# dicionário. Depois, o usuário deve digitar o nome de um aluno. Se ele existir:
# a. aumente sua nota em 1 ponto, sem ultrapassar 10;
# b. exiba o dicionário atualizado.
# Se o aluno não existir, exiba "Aluno não encontrado".
# Execução simulada:
# Entrada:
# Digite o nome do aluno: Ana
# # Saída:
# {'Ana': 10, 'João': 7}

alunos = {
    'Ana': 9,
    'João': 7
}

print("Alunos cadastrados:", alunos)

nome = input('\nDigite o nome do aluno: ')

if nome in alunos:
    if alunos[nome] < 10:
        alunos[nome] = alunos[nome] + 1
    
    print(alunos)
else:
    print("Aluno não encontrado")