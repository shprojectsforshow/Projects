person = "dave"
coins = 3 

message = "\n%s has %s coins left" % (person,coins)
print(message)

message = "\n{} has {} coins left".format(person,coins)
print(message)

message = "\n{0} has {1} coins left".format(person,coins)
print(message)

message = "\n{person} has {coins} coins left".format(
    person=person,coins=coins
)
print(message)

player = { 'person': 'dave', 'coins': 3}

message = "\n{person} has {coins} coins left".format(**player)
print(message)

##################

message = f"\n{person} has {coins} coins left"
print(message)

message = f"\n{person} has {2 * 5} coins left"
print(message)

message =  f"\n{person.lower()} has {2 * 5} coins left"
print(message)

message =  f"\n{player['person']} has {2 * 5} coins left"
print(message)

#passing formatting options

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1,11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")