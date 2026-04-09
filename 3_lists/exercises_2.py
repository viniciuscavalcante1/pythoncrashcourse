"""
3.4 Lista de convidados: Se pudesse convidar qualquer pessoa, viva ou falecida, para um jantar, quem você convidaria? Crie uma lista que tenha pelo menos três pessoas que gostaria de convidar para um jantar. Em seguida, use sua lista a fim de exibir uma mensagem para cada pessoa, convidando-a para o jantar.

Matthes, Eric. Curso Intensivo de Python - 3ª edição: Uma Introdução Prática e Baseada em Projetos à Programação (Portuguese Edition) (p. 93). (Function). Kindle Edition.
"""

persons = ['Milton', 'Socorro', 'Bruna']
print(f'Gostaria de convidar você para jantar, {persons[0]}')
print(f'Gostaria de convidar você para jantar, {persons[1]}')
print(f'Gostaria de convidar você para jantar, {persons[2]}')

"""
3.5 Mudando a lista de convidados: Você acabou de ficar sabendo que um dos convidados não conseguirá ir ao jantar, assim precisa enviar um conjunto novo de convites. É necessário convidar outra pessoa.

Comece com o programa do Exercício 3.4. No final do programa, adicione um print(), informando o nome do convidado que não irá ao jantar. • Modifique sua lista substituindo o nome do convidado que não pode comparecer pelo nome da pessoa nova que você está convidando. • Exiba um segundo conjunto de mensagens de convite, uma para cada pessoa que ainda não consta em sua lista.

Matthes, Eric. Curso Intensivo de Python - 3ª edição: Uma Introdução Prática e Baseada em Projetos à Programação (Portuguese Edition) (p. 93). (Function). Kindle Edition. 
"""

will_not_dinner = persons.pop()
print(f"Infelizmente a {will_not_dinner} não poderá participar")

persons.append('Linda')
print(f'Gostaria de convidar você para jantar, {persons[2]}')

"""
3.6 Mais convidados: Você acabou de encontrar uma mesa maior de jantar, agora há mais espaço disponível. Convide mais três pessoas para o jantar. • Comece com o programa do Exercício 3.4 ou 3.5. No final do programa, adicione um print(), informando às pessoas que encontrou uma mesa maior. • Use um insert() para adicionar um convidado novo ao início de sua lista. • Use um insert() para adicionar um convidado novo no meio de sua lista. • Use um append() para adicionar um convidado novo no final de sua lista. • Exiba um conjunto novo de mensagens de convite, um para cada pessoa em sua lista.

Matthes, Eric. Curso Intensivo de Python - 3ª edição: Uma Introdução Prática e Baseada em Projetos à Programação (Portuguese Edition) (pp. 93-94). (Function). Kindle Edition. 
"""

print("Encontramos uma mesa maior!")
persons.insert(0, 'Mariana')
persons.insert(1, 'Mariana')
persons.append('Mariana')

print(f'Gostaria de convidar você para jantar, {persons[0]}')
print(f'Gostaria de convidar você para jantar, {persons[1]}')
print(f'Gostaria de convidar você para jantar, {persons[-1]}')

"""
3.7 Reduzindo a lista de convidados: Você acabou de descobrir que sua mesa nova de jantar não chegará a tempo e agora tem espaço somente para dois convidados. • Comece com o programa do Exercício 3.6. Adicione uma linha nova que exiba uma mensagem que você pode convidar apenas duas pessoas para o jantar. • Use o pop() para remover convidados de sua lista, um de cada vez, até que restem somente dois nomes nela. Sempre que remover um nome de sua lista, exiba uma mensagem para essa pessoa informando que lamenta por não poder convidá-la para o jantar. • Exiba uma mensagem para cada uma das duas pessoas que ainda estão na sua lista, informando que ainda estão convidadas. • Use o del para remover os dois últimos nomes de sua lista, para que ela fique vazia. Exiba sua lista para ter certeza de que você realmente tem uma lista vazia no final do seu programa.

Matthes, Eric. Curso Intensivo de Python - 3ª edição: Uma Introdução Prática e Baseada em Projetos à Programação (Portuguese Edition) (p. 94). (Function). Kindle Edition. 
"""

print("Puts, só dá pra convidar duas pessoas!")

print(f"Lamento, {persons.pop(0)}, mas a mesa foi cancelada e não poderemos mais jantar :(")
print(f"Lamento, {persons.pop(0)}, mas a mesa foi cancelada e não poderemos mais jantar :(")
print(f"Lamento, {persons.pop()}, mas a mesa foi cancelada e não poderemos mais jantar :(")
print(f"Lamento, {persons.pop()}, mas a mesa foi cancelada e não poderemos mais jantar :(")
print(f"{persons[0]}, você ainda está no convite para jantarmos!")
print(f"{persons[1]}, você ainda está no convite para jantarmos!")
del persons[0]
del persons[0]
print(persons)