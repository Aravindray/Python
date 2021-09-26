print("Is Raining?")
user = input("")
if user == "yes":
    print("Have Umbrella?")
    user1 = input("")
    if user1 == "yes":
        print("Go Outside")
    else:
        print("wait a while")
        print("Is Raining?")
        user2 = input("")
        if user2 == "yes":
            print("Wait a while")
        else:
            print("Go outside")
else:
    print("Go outside")