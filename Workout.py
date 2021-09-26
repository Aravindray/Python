import random
Numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]


# print(random.choices(Numbers))
# print(random.sample(Numbers,25))

# Useful Hint = ^[A-Za-z]+$ (this is what called regex)


Key_Words = ['cranes',
'turnaround',
'1000',
'Liner',
'cross-sections',
'turnaround',
'Containerisation',
'containers',
'productivity',
'shipping',
'movement',
'container',
'connectivity',
'tracking',
'vessel',
'Insured',
'storage',
'management',
'German',
'owning',
'Twenty-foot Equivalent','Forty-foot Equivalent',
'temporary',
'tanks',
'interchange',
'inland'
]

# print(random.sample(Key_Words,25), end = ', ')
print("Keywords: ", end=' ')
for i in range(25):
    i = random.randrange(1,25)
    print(Key_Words[i],end =', ')
