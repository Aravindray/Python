# copy() and deepcopy() module function

import copy

spam = ['a','b','c','d']
print(id(spam))

cheese = copy.copy(spam)
print(id(cheese))
print(cheese)
cheese[1] = 42

print(spam)
print(cheese)