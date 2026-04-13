"""
5.9 Sem usuários: adicione um teste if a hello_admin.py a fim de garantir que a lista de usuários não esteja vazia.

Se a lista estiver vazia, exiba mensagem: É necessário encontrar alguns usuários!
Remova todos os nomes de usuários de sua lista e verifique se a mensagem correta foi exibida.
"""

users = ['admin', 'bruna', 'milton', 'socorro', 'benjamin', 'clara']

if users:
    for user in users:
        if user == 'admin':
            print('Olá, admin, gostaria de ver um relatório de status?')
        else:
            print(f"Olá, {user}")
else:
    print('É necessário encontrar alguns usuários!')