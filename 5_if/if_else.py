cars = ['audi', 'bmw', 'mercedes', 'jaguar']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif car == 'jaguar':
        print(car.lower())
    else:
        print(car.title())

# conditional tests
car = 'bmw'
print(car == 'bmw')
print(car != 'bmw')

age = 20
print(age > 18)
print(age >= 20)
print(age < 18)
print(age <= 20)

print((car == 'bmw') and (age >= 18))
print((age <= 18) or (car == 'mercedes'))

# multiple

toppings = ['Coco', 'Amendoim', 'Granola']
if 'Coco' in toppings:
    print('Coco adicionado!')
if 'Amendoim' in toppings:
    print('Amendoim adicionado!')
if 'Granola' in toppings:
    print('Granola adicionado!')
print('Açaí pronto!')