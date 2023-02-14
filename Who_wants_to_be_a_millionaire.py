questions = [
    ("Which Disney character famously leaves a glass slipper behind at a royal ball?", "Cinderella"),
    ("What is the largest ocean in the world?", "Pacific Ocean"),
    ("What name is given to the revolving belt machinery in an airport that delivers "
     "checked luggage from the plane to baggage reclaim?", "Carousel"),
    ("Which toys have been marketed with the phrase “robots in disguise”?", "Transformers"),
    ("Obstetrics is a branch of medicine particularly concerned with what?", "Childbirth")
]


def game():
    print("Welcome to Who Wants to Be a Millionaire!\n")
    score = 0
    for question, answer in questions:
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        if user_answer.lower() == answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}\n")
            break
    print(f"You scored {score} points out of {len(questions)}")


game()
