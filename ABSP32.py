# Practice Project

# Comma Seperation
import copy

def demo(like):
    for i in range(len(like)-1):
        print(str(like[i]) + ',' ,end=' ')
    print('and '+str(like[-1]))
        

look = []

''' while True:
    print('Enter the input: ')
    demo = input()
    if demo =='':
        break
    look = look + [demo]
print(look)
print(type(look)) '''

demo(look)