# Converting Types with the list() and tuple() Functions

print(tuple(['cat', 'dog', 5]))

print(list(('cat', 'dog', 5)))

print(list('hello'))

# Passing References

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam)