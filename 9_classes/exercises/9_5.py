# 9.5 Tentativas de login: Adicione um atributo chamado login_attempts à sua classe User do
# Exercício 9.3. Crie um método chamado increment_login_attempts() que incrementa o valor
# de login_attempts em 1. Crie outro método chamado reset_login_attempts() que redefine o
# valor de login_attempts para 0.
# Crie uma instância da classe User e chame increment_login_attempts() diversas vezes. Exiba
# o valor de login_attempts para verificarque foi incrementado corretamente e, em seguida,
# chame reset_login_attempts(). Exiba login_attempts novamente a fim de ter certeza de que
# foi redefinido para 0.

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(f"First name: {self.first_name}. Last name: {self.last_name}")

    def greet_user(self):
        print(f"Hi, {self.first_name}!")

user = User(first_name='Vi', last_name='Cavalcante')

user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)

user.reset_login_attempts()
print(user.login_attempts)