def grade_system():
    if grade == 9:
        print("You're a Freshman")
    elif grade == 10:
        print("You're a Sophomore")
    elif grade == 11:
        print("You're a Junior")
    elif grade == 12:
        print("You're a Senior")
    else:
        print("TBD")


grade = int(input("What's your grade?\n(numbers only)\n-->"))
grade_system()
