cars = ['Polo', 'Gol', 'Palio']
print(cars) # ['Polo', 'Gol', 'Palio']

# accessing elements
print(cars[0]) # Polo

# last element
print(cars[-1]) # Palio

# changing elements
cars[0] = 'Santana'
print(cars[0]) # Santana

# appending elements
cars.append('Uno')
print(cars[-1]) # Uno

# adding elements to specific position
cars.insert(0, 'Mobi')
print(cars[0]) # Mobi

# deleting elements
del cars[0]
print(cars[0]) # Santana

# with pop
popped_car = cars.pop()
print(popped_car) # Uno

# pop index
popped_car = cars.pop(1)
print(popped_car) # Gol

# by value
print(cars) # ['Santana', 'Palio']
cars.remove('Santana')
print(cars) # ['Palio']

# sort
cars = ['bmw', 'audi', 'mercedes', 'toyoota']
cars.sort() # altera permanentemente a ordem da lista
print(cars) # ['audi', 'bmw', 'mercedes', 'toyoota']
cars.sort(reverse=True)
print(cars) # ['toyoota', 'mercedes', 'bmw', 'audi']
sorted(cars) # ['toyoota', 'mercedes', 'bmw', 'audi']

# reverse
cars.reverse()
print(cars) # ['audi', 'bmw', 'mercedes', 'toyoota']

# len
print(len(cars)) # 4