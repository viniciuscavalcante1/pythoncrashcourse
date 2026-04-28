def greet_user(username): # parameter
    """Greet an user"""
    print(f"Hello, {username.title()}!")

greet_user("vini") # argument

def describe_pet(pet_name, animal_type='cachorro'):
    print(f"Eu tenho um {animal_type} chamado {pet_name.title()}")

# positional argument
describe_pet('hamster', 'Tom')

# named argument
describe_pet(animal_type='gato', pet_name='gato')

# default
describe_pet('dog')

# return
def get_formatted_name(first_name, last_name):
    """Retorna um nome completo"""
    return f"{first_name} {last_name}".title()

vini = get_formatted_name("Vinícius", 'Cavalcante')
print(vini)

# optional
def get_formatted_name(first_name, last_name, middle_name=""):
    """Retorna um nome completo"""
    return f"{first_name} {middle_name} {last_name}".title() if middle_name else f"{first_name} {last_name}".title()

vini = get_formatted_name("Vinícius", 'Cavalcante')
print(vini)
vini = get_formatted_name('Vinícius', 'Cavalcante', 'de Abreu')
print(vini)

# arbritary number of arguments
def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni', 'teste')

# arbritary named arguments
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)