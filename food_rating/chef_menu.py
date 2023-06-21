def restaurant_average():
    with open('rating.txt', 'r') as file:
        rates = []
        for line in file:
            rate = line.split(',')[0]
            rates.append(int(rate))

        if len(rates) > 0:
            media = sum(rates) / len(rates)
            return media
        else:
            return 0


nota_restaurante = restaurant_average()
print(f"A média das notas do restaurante é: {nota_restaurante}")
