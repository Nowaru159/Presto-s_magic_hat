import random

quotes = [
    "Don’t hold onto things that require a tight grip.",
    "I didn’t come this far to only come this far.",
    "Vulnerability sounds like faith and looks like courage.",
    "And into the forest I go, to lose my mind and find my soul.",
    "Do it scared.",
    "Look how far you've come.",
    "Each time you break your own boundaries to ensure that someone else likes you, you like yourself a little less.",
    "Sitting in silence with you is all the noise I need.",
    "There is nothing stronger than a broken woman who has rebuilt herself.",
    "Be careful who you trust. Salt and sugar look the same."
]

while True:
    question = input("Do you  want to see your fortune?\n").lower()
    if question.lower() == "no":
        break
    elif question.lower() == "yes":
        print(random.choice(quotes))
    else:
        print("What?")
        question = input("One more ?\n").lower()

print("Hmm... You're full of wisdom now")
