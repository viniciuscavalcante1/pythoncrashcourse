# as a queue
unconfirmed_users = ['vini', 'bru', 'socorro']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user {current_user.title()}")
    confirmed_users.append(current_user)

print("The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# remove elements
pets = ['dog', 'cat', 'cat', 'cat', 'cat', 'cat', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    print('removing cat')

print(pets)