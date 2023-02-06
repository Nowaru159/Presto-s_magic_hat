print("======== Secret door========")
print("shhhhhh, what you want ? \n To enter here you need to say the secretword..")
print("It's a round ghost type pokemon")


pin = str(input("What's the secret word?\n")).lower()

while pin != "gastly":
    pin = str(input("Incorret!\n Suspicious...\n What's the secret word?\n")).lower()
    if pin == "gastly":
        print("A person of culture, you are\n You may enter...")
