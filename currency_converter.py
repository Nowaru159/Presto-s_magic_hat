def converter(amount,currency):
    if currency == "CH":
        return 0.76 * amount
    elif currency == "JP":
        return 0.039 * amount
    elif currency == "KR":
        return 0.0041 * amount
    elif currency == "US":
        return 5.14 * amount

print("Hmmm.. I see... there are some money in your bag...\n I will help you to converter" )

yuan = float(input("Enter the chinese yuan: "))
yen = float(input("Enter the japanese yen: "))
won = float(input("Enter the korean won: "))
dolar = float(input("Enter the american dolar: "))

real = converter(yuan,"CH") + converter(yen,"JP") + converter(won,"KR") + converter(dolar,"US")

print("The total amount in brazilian real is: R$%.2f" % real)