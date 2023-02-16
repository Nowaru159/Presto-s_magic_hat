def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOU":
            translation = translation + "F"
        elif letter in "aeiou":
            translation =  translation + "f"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))