
ph = int(input("Please, input the pH value (0 - 14): "))

if ph > 7 and ph <= 14:
    print("Basic")
elif ph >= 0 and ph < 7:
    print("Acidic")
elif ph == 7:
    print("Neutral")
else:
    print("ERROR")
