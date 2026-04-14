alien_0 = {'color': 'green', 'points': 10}
alien_1 = {'color': 'yellow', 'points': 15}
alien_2 = {'color': 'red', 'points': 20}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens: print(alien)

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 15
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 20
        alien['speed'] = 'fast'

print(aliens)

pizza = {
    'massa': 'fina',
    'ingredientes': ['muçarela', 'calabresa']
}

print(f'Você pediu uma pizza de massa {pizza['massa']} com os ingredientes {", ".join(pizza['ingredientes'])}')

favorite_languages = {
    'jen': ['python', 'c'],
    'vi': ['python', 'go']
}

for k, v in favorite_languages.items():
    print(f"As linguagens favoritas do {k} são {", ".join(v).title()}")

users = {
    'vini': {
        'first': 'vini',
        'last': 'cavalcante',
        'location': 'sp'
    },
    'hasan': {
        'first': 'hasan',
        'last': 'zaibak',
        'location': 'syria'
    }
}

for username, info in users.items():
    print(f'username {username}')
    full_name = f"{info['first']} {info['last']}"
    location = f"{info['location']}"
    print(f'full name {full_name}')
    print(f'location {location}')