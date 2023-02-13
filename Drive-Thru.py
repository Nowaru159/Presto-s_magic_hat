def menu_item(item):
    if item == 1:
        return "Apple"
    elif item == 2:
        return "Kiwi"
    elif item == 3:
        return "Banana"
    elif item == 4:
        return "Pear"
    elif item == 5:
        return "Grape"
    elif item == 6:
        return "Strawberry"
    else:
        return "ERROR"


def menu_price():
   print("1-Apple $4,99\n2-Kiwi $8,99\n3-Banana $6,99\n4-Pear $10,00\n5-Grape $25,00\n6-Strawberry $25,00\n")


print("Welcome to Good Juice!\n Here's the menu:\n")
menu_price()

order = int(input("Please input the number of your juice choice:\n"))
print(menu_item(order) + " juice")
print("Thank you for choosing Good Juice, your juice will be ready in a few seconds")
