def is_palindrome(number):
    number_str = str(number)
    reversed_str = number_str[::-1]

    return number_str == reversed_str

num = int(input("Digite um número: "))

if is_palindrome(num):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")
