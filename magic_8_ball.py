import random


answers = [
    "Yes - definitely",
    "It is decidedly so",
    "Without a doubt",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful."
]

print("MAGIC 8 BALL: Ask me , the grater wisdom, anything\n")
print("Make a question or digit exit to quit.")

while True:
    question = input("Your question: ").lower()
    if question.lower() == "exit":
        break
    print(random.choice(answers))

print("You shall exit now!")
