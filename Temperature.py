def cel_to_far(far):
    far = (cel * 9 / 5) + 32
    return far

def far_to_cel(cel):
    cel = (far - 32) * 5 / 9
    return cel

choice = int(input("Master, if you want to converter Celcius to Fahrenheit,put 1  or if you want to converter Fahreinheit to Celcius, put 2 :\n"))

if choice == 1:
    cel = float(input("Enter the temperature in Celsius: "))
    far = cel_to_far(cel)
    print("Temperature in Fahrenheit: ", far)

elif choice == 2:
    far = float(input("Enter the temperature in Fahrenheit: "))
    cel = far_to_cel(far)
    print("Temperature in Celcius: ", cel)

else:
    print("you hit the self destruct buttoooooooon\n F\n X_X")



