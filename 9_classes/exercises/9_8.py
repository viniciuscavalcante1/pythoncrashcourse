# 9.8 Privilégios: Crie uma classe Privileges separada. A classe deve ter um atributo,
# privileges, que armazene uma lista de strings, conforme descrito no Exercício 9.7.
# Passe o método show_privileges() para essa classe. Crie uma instância de Privileges
# como um atributo na classe Admin. Crie uma instância nova de Admin e use seu método
# para mostrar seus privilégios.

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)

from user_9_5 import User

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name=first_name, last_name=last_name)
        self.privileges = Privileges('can ban user')

admin = Admin('Vi', 'Cavalcante')
admin.privileges.show_privileges()