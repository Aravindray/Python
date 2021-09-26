# Rock, Paper, Scissor Game

import random, sys

print("Welocme to Rock, Paper, Scissor Game")

win = 0 
loss = 0
tie = 0

while True: #Main game loop
    print('%s Win, %s Loss, %s Tie'%(win,loss,tie))
    while True:
        print("Enter your choice Rock, Paper, Scissor or Quit")
        user = input()
        if user == 'Quit':
            print("You typed " + user + ". So See you later.")
            sys.exit()
        if user == 'Rock' or user == 'Paper' or user == 'Scissor':
            break
        print("Type one of this: Rock Paper Scissor")
# Users Choice
    if user =="Rock":
         print("Rock versus.....")
    elif user == "Paper":
         print("Paper versus....")
    elif user == "Scissor":
         print("Scissor versus.....")
# Computer Choice
    Computer = random.choice(["Rock","Paper","Scissor"])
    if Computer == "Rock":
         print("Rock")
    elif Computer == "Paper":
         print("Paper")
    elif Computer == "Scissor":
         print("Scissor")
# Result
    if user == Computer:
         print("Ties")
         tie = tie + 1
    elif user == "Rock" and Computer == "Scissor":
         print("You Win")
         win = win + 1
    elif user == "Paper" and Computer == "Rock":
         print("You Win")
         win = win + 1
    elif user == "Scissor" and Computer == "Paper":
         print("You win")
         win = win + 1
    elif user == "Rock" and Computer == "Paper":
         print("Loss")
         loss = loss + 1
    elif user == "Paper" and Computer == "Scissor":
         print("Loss")
         loss = loss + 1
    elif user == "Scissor" and Computer == "Rock":
         print("Loss")
         loss = loss + 1