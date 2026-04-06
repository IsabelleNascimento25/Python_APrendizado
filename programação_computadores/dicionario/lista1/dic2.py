#  O programa deve permitir que o usuário cadastre nomes e números de
# telefone em um dicionário, onde os nomes são as chaves e os números são
# os valores. Após o cadastro, o programa deve solicitar que o usuário digite o
# nome de um contato e exibir o número de telefone correspondente. Caso o
# contato não esteja no dicionário, exiba a mensagem "Contato não
# encontrado".
# Exemplo de execução:
# Entrada (cadastro):
# Nome: Maria → Telefone: 7777-3333
# Nome: João → Telefone: 8888-2222
# Entrada (consulta): Maria
# Saída: 7777-3333
# Outro exemplo:
# Entrada (cadastro):
# Nome: Maria → Telefone: 7777-3333
# Nome: João → Telefone: 8888-2222

dic = {
    'Maria' : '7777-3333',
    'João' :'8888-2222',
}
entrada = input('Digite um nome: (Maria), (João) ')

if entrada in dic:
    print (dic[entrada])
else:
    print('Nome nao encontrado')