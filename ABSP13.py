# Return Values
# Magic ball 8 
import random

def values(number):
    if number == 1:
        return 'It is certain'
    elif number == 2:
        return 'It is decidedly so'
    elif number== 3:
        return "Okay, That's enough"
    elif number == 4:
        return None

like = random.randint(1,4)
notlike = values(like)
print(notlike)

'''since you can pass return values as an argument
to another function call, you could shorten above three lines like this'''

print(values(random.randint(1,4)))