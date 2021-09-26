# Sequence Data Types

''' strings and lists are actually similar
if you consider a string to be a “list” of single text characters'''

name = 'Zophie'
print(name[0])
print(name[-2])
print(name[0:4])
if 'Zo' in name:
    print('yes')
if 'z' in name:
    print('yes')
else:
    print('no')
if 'p' not in name:
    print('yes')
else:
    print('no')
for i in name:
    print('* * * ' + i + ' * * *')

''' Mutable and Immutable Data Types
But lists and strings are different in an important way.
A list value is a mutable data type: it can have values added, removed, or changed.
However, a string is immutable: it cannot be changed.'''