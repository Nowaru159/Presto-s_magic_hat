rate = str(input("E o que você achou da nossa comida ?\n"
                 "1 - Péssima\n"
                 "2 - Meia Boca\n"
                 "3 - Boa\n"
                 "4 - Excelente\n"
                 "5 - Extraordinária\n"))

sugestion = str(input("Nos dê a sua sugestão ou reclamação, por favor\n"))

print("Agradecemos a sua opinião!")

with open('rating.txt', 'a') as arc:
    arc.write(rate + "," + sugestion + "\n")
