"""
5.10 Verificando nomes de usuários:
faça o seguinte para criar um programa que simule como os sites garantem que todos tenham um nome de usuário exclusivo.

Crie lista de cinco ou mais nomes de usuários chamada current_users.
Crie outra lista com cinco nomes de usuários chamada new_users.
Assegure-se de que um ou dois dos nomes novos de usuário também estejam na lista current_users.
Percorra com um loop a lista new_users para verificar se cada nome novo de usuário já foi usado.
Se sim, exiba uma mensagem informando que a pessoa precisará inserir um nome novo de usuário.
Se um nome de usuário não foi usado, exiba uma mensagem informando que o nome de usuário está disponível.
Garanta que sua comparação não diferencie letras maiúsculas de minúsculas.
Se 'John' foi usado, 'JOHN' não deve ser aceito.
(Para fazer isso, será necessário fazer uma cópia de current_users contendo as versões
em minúsculas de todos os usuários existentes.)
"""

current_users = ['admin', 'bruna', 'milton', 'socorro', 'benjamin', 'clara']
lower_current_users = [user.lower() for user in current_users]
new_users = ['benjamin', 'clara', 'antoine', 'hasan', 'mariana']

for user in new_users:
    if user.lower() in lower_current_users:
        print(f"Já existe um usuário {user}, escolha outro.")
    else:
        print(f"O usuário {user} está disponível.")