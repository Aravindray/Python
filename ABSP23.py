# Using for loop in lists
# in and not in operators

catName = []
while True:
    print("Enter the Name or just click enter to exit")
    name = input()
    if name == '':
        break
    catName = catName + [name]
print('cat name are:')
for name in catName:
    print(' '+name)
print(catName)
print('Enter which name do you want to find out')
user = input()
if user not in catName:
    print(user + ' not in the list')
else:
    print(user + ' is in the list')

# Using the enumerate() Function with Lists

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

# Using the random.choice() and random.shuffle() Functions with Lists

import random
pets = ['Dog', 'Cat', 'Moose']
random.choice(pets)

# random suffle

people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
print(people)