# while and continue

while True:
    print("Who are you?")
    name = input()
    if name != 'Hey':
        continue
    print("Hello, " + name + " what is the password?")
    password = input()
    if password == "Good":
        break
print("Access Granted")

# Weird One
 
''' name = ''
while not name:
    print("Enter your name")
    name = input()
print("How many guests will you have?")
numofguests = int(input())
if numofguests:
    print('Be sure to have enought room for all the guests.')
print('Done') '''