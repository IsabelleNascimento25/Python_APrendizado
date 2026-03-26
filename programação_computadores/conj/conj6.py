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