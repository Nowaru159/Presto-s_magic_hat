print("Welcome, master ! \nI will assist you in your counts!")
num1= float(input("Now, please, enter your first number: "))
op =input("The operator,please: ")
num2= float(input("And finally your number last number: "))



def operator_discover():
    print("Here your result, master: ")
    if op == "+":
       print(num1+num2)

    elif op == "-":
        print(num1-num2)

    elif op == "x" or op =="*":
        print(num1 * num2)

    elif op == "/":
        print(num1 / num2)

    elif op == "^":
        print(num1**num2)

    else:
        print("Sorry , I don't know what you mean  T^T")

operator_discover()

