def bmi_calculator(mass,height):
    bmi = mass/height**2
    return bmi


print("Hi, I will calculate your bmi , but i need a few things before...\n")
mass   = float(input("Please, insert your mass in KG: "))
height = float(input("Now I need your heigh in meters: "))
bmi    = bmi_calculator(mass, height)
print("Your bmi is : ", bmi)

if bmi <18.5:
    print("You are underweight ")

elif bmi >= 18.5 and bmi <= 24.9:
    print("You are healthy! ")

elif bmi >= 25 and bmi <= 29.9:
    print("You are overweight ")

elif bmi >= 30 and bmi <= 39.9:
    print("You are obese ")

else:
    print("You are extremely obese ")


