def roman_to_int(r):
    roman_values = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    result = 0
    n = len(r)

    for i in range(n):

        if i < n - 1 and roman_values[r[i]] < roman_values[r[i + 1]]:
            result -= roman_values[r[i]]
        else:
            result += roman_values[r[i]]

    return result

number = input("Digite o número romano: ").upper()
print(roman_to_int(number))
