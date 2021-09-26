''' Good = open("Text.txt","r")
Rase = Good.read()
print(Rase)
Good.close() '''

'''Marvel = open("Text.txt","w")
Marvel.write("Welcome Aravind")
Marvel.close()'''

# For Write
Write = open("Text.txt","w")
Write.write("Hello, Everyone!")
Write.close()

# For Read
Write1 = open("Text.txt", "r")
Read = Write1.read()
print(Read)
Write1.close()

# Append
Write2 = open("Text.txt","a")
Write2.write("Next Line")
Write2.close()