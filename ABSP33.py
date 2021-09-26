# Practice Project

# Flip Coin Project

import random

Coin = []
Flips = ["H","T"]
HeadCount = 0
TailCount = 0

for i in range(100):
    demo = random.choice(Flips)
    Coin = Coin + [demo]

print(Coin)
print(len(Coin))

for i in range(100):
    if Coin[i] == 'H':
        HeadCount += 1
    elif Coin[i] == 'T':
        TailCount += 1

print("Head Counts are: " + str(HeadCount))
print("Tail Counts are: " + str(TailCount))

Flips = 0

for i in range(99):
    for Flips in range(6):
        if Coin[i] == Coin[i+1]:
            Flips +=1
        
if Flips == 6:
    print('Stricks')

# Honestly, I don't quit understand what the question was, so I came up for this
# this program print 'Stricks' if head or tail flips 6 in a row


''' # this is for 1000 times and finds out 100 time in row

import random

Coin = []
Flips = ["H","T"]
HeadCount = 0
TailCount = 0

for i in range(1000):
    demo = random.choice(Flips)
    Coin = Coin + [demo]

print(Coin)
print(len(Coin))

for i in range(1000):
    if Coin[i] == 'H':
        HeadCount += 1
    elif Coin[i] == 'T':
        TailCount += 1

print("Head Counts are: " + str(HeadCount))
print("Tail Counts are: " + str(TailCount))

Flips = 0

for i in range(999):
    for Flips in range(100):
        if Coin[i] == Coin[i+1]:
            Flips +=1
        
if Flips == 100:
    print('Stricks') '''