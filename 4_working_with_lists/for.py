names = ['Ben', 'Clara']
for name in names:
    print(name)

# range

for value in range(1, 5):
    print(value)

values = range(1, 5)
print(values) # range(1, 5)
values = list(values)
print(values) # [1, 2, 3, 4]

# range with step

even_numbers = list(range(2, 9, 2))
print(even_numbers)