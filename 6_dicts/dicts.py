# defining
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'], alien_0['points']) # green 5

# accessing keys
new_points = alien_0['points']
print(f"Você ganhou {new_points} pontos!") # Você ganhou 5 pontos!

# new values
print(alien_0) # {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) # {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

# empty
empty = {}
print(empty) # {}

# modifying
print(f"The alien is {alien_0['color']}") # The alien is green
alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}") # The alien is yellow

alien_0['speed'] = 'medium'
print(f'Original alien position: x {alien_0['x_position']} y {alien_0['y_position']}')
# Original alien position: x 0 y 25

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f'New alien position: x {alien_0['x_position']} y {alien_0['y_position']}')
# New alien position: x 2 y 25

# removing
del alien_0['points']
print(alien_0) # {'color': 'yellow', 'x_position': 2, 'y_position': 25, 'speed': 'medium'}

# similar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'ruby',
}

person = 'jen'
favorite_language = favorite_languages[person].title()
print(f"{person.title()}'s favorite language is {favorite_language}")

# accessing key that don't exist
print(alien_0) # {'color': 'yellow', 'x_position': 2, 'y_position': 25, 'speed': 'medium'}
# print(alien_0['gun']) # KeyError: 'gun'
print(alien_0.get('gun', 'No gun equipped.')) # No gun equipped.

# items
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f'\nkey: {key}') # key: last
    print(f'value: {value}') # value: fermi

# keys
friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    if name in friends:
        language = favorite_languages[name].title()
        print(f'Hi, {name.title()}! I see that you like {language}!')

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')

print(sorted(favorite_languages.keys()))

# values
print("The following languages were mentioned:")
for language in sorted(favorite_languages.values()): print(language.title())

# with set
for language in sorted(set(favorite_languages.values())): print(language.title())