secret_word = "cute".lower()
guess = ""
guess_count     = 0
guess_limit     = 2
out_of_guesses  = False

while guess != secret_word:
    print("One of various things that Nowaru is...?")
    guess = str(input("Enter guess: ")).lower()
    if guess !=secret_word:
        if guess_count <guess_limit:
            print("Nop , try again")
            guess_count +=1
        elif guess != secret_word and guess_limit ==2:
            out_of_guesses = True
            print("Enough!... Tsk..")
            exit()
    else:
        print("Heheh, How cute of you.")
