# 9.3 Usuários: Crie uma classe chamada User. Crie dois atributos chamados first_name
# e last_name e diversos outros atributos que normalmente são armazenados em um perfil
# de usuário. Crie um método chamado describe_user() que exiba um resumo das informações
# do usuário. Crie outro método chamado greet_user() que exiba um cumprimento personalizado
# ao usuário. Crie diversas instâncias que representem usuários distintos e chame ambos
# os métodos para cada um.

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"First name: {self.first_name}. Last name: {self.last_name}")

    def greet_user(self):
        print(f"Hi, {self.first_name}!")

user = User(first_name='Vi', last_name='Cavalcante')
user1 = User(first_name='Vi1', last_name='Cavalcante')
user2 = User(first_name='Vi2', last_name='Cavalcante')
user3 = User(first_name='Vi3', last_name='Cavalcante')
user4 = User(first_name='Vi4', last_name='Cavalcante')

user.greet_user()
user2.greet_user()
user3.greet_user()
user4.greet_user()

