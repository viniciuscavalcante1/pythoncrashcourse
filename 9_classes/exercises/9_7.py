# 9.7 Admin: Um administrador é um tipo especial de usuário. Crie uma classe chamada Admin
# que herde da classe User escrita no Exercício 9.3 ou Exercício 9.5. Adicione um atributo,
# privileges, que armazene uma lista de strings como "can add post", "can delete post",
# "can ban user", e assim por diante. Escreva um método chamado show_privileges() que
# enumere o conjunto de privilégios do administrador. Crie uma instância Admin e chame
# seu método.

from user_9_5 import User

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name=first_name, last_name=last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)

admin = Admin('Vi', 'Cavalcante')
admin.show_privileges()