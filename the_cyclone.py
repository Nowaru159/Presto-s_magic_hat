height = int(input("Adicione sua altura em cm:\n"))
credits = int(input("Quantos créditos vc possui?\n"))

if height >= 137 and credits >= 10:
    print("Divirta-se")

elif height < 137:
    print("Você não tem altura o suficiente para o brinquedo")

elif credits < 10:
    print("Você não possui créditos o suficiente")

else:
    print("Dados inválidos")