x = "Awesome"

def myfunc():
    x = "fantastic"
    global y
    y ="Hello"
    print("Python is " + x)

myfunc()

print(y)
print(x)