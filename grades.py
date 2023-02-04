grade = int(input("Put your grade please:"))

if grade >=0 and grade <=69:
    print("You failed, have to study more...")
elif grade>=70 and grade<= 100:
    print("Congratulations! You passed!")
else:
    print("ERROR")