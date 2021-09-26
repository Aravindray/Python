# Methods

# Finding a Value in a List with the index() Method

spam1 = ['hello', 'hi', 'howdy', 'heyas']

print(spam1.index('hello'))
print(spam1.index('heyas'))
# print(spam1.index('howdy howdy howdy'))

# Repeated items in list

spam2 = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(spam2.index('Pooka'))

# Adding Values to Lists with the append() and insert() Methods

spam3 = ['cat', 'dog', 'bat']
spam3.append('moose')
print(spam3)

# using insert method

spam4 = ['cat', 'dog', 'bat']
spam4.insert(1, 'chicken')
print(spam4)

# EXCEPTIONS TO INDENTATION RULES IN PYTHON

spam = ['apples',
    'oranges',
                    'bananas',
'cats']
print(spam)

#  \ line continuation character

print('Four score and seven ' + \
      'years ago...')