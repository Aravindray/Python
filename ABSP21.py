# The collatz sequence
# My first program I did it all myself
import sys, time

def collatz(number):
    if number == 1:
        sys.exit()
    elif number % 2 == 0:
        a = number // 2
        print(a)
        time.sleep(0.1)
        collatz(a)
    elif number % 2 == 1:
        b = 3 * number + 1
        print(b)
        time.sleep(0.1)
        collatz(b)
    
print("Enter Input: ")
UserInput = int(input())
collatz(UserInput)

# My first Program