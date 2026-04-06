#  O programa deve criar um dicionário chamado funcionario a partir dos
# dados digitados pelo usuário. O usuário deve informar o nome, o cargo e o
# salário inicial do funcionário. Após exibir o dicionário com os dados
# cadastrados, o programa deve perguntar se o usuário deseja atualizar o
# salário. Caso a resposta seja sim, deve solicitar o novo salário e atualizar o
# valor correspondente no dicionário. Caso a resposta seja não, o salário deve
# permanecer inalterado.
# Exemplo de execução 1 (com atualização):
# Entrada:
# Nome: Ana
# Cargo: Gerente
# Salário inicial: 7000
# Deseja atualizar o salário? s
# Novo salário: 7500
# Saída: {'nome': 'Ana', 'cargo': 'Gerente', 'salario': 7500}

nome = input('Digite nome: ')
cargo = input('Digite Cargo: ')
salario = int(input('Digite o salário: '))

funcionarios = {
    'nome': nome,
    'cargo': cargo,
    'salario': salario
}

print(funcionarios)

mudanca = input('Quer mudar algo? escolha 1 para nome 2 para cargo 3 para salario e (n) para prosseguir: ')

if mudanca == '1':
    new_nome = input('Digite outro nome: ')
    funcionarios['nome'] = new_nome

elif mudanca == '2':
    new_cargo = input('Digite outro cargo: ')
    funcionarios['cargo'] = new_cargo

elif mudanca == '3':
    new_salario = int(input('Digite o novo salário: '))
    funcionarios['salario'] = new_salario

elif mudanca == 'n' or mudanca == 'N':
    print('Nenhuma alteração realizada.')

else:
    print('Opção inválida!')

print(f'Atualizado funcionario: {funcionarios}')