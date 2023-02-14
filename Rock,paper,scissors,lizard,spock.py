import random

def game():
    plays = ['rock',
             'paper',
             'scissors',
             'spock',
             "lizard"
             ]
    cpu_play = random.choice(plays)
    player_play = str(input("Choose your play: rock, paper, scissors, spock or lizard?\n")).lower()
    print("Ai plays: " + cpu_play)

    if player_play == cpu_play:
        print("Draw!")
    elif player_play == 'scissors' and cpu_play == 'paper':
        print("You win!!!!")
    elif player_play == 'paper' and cpu_play == 'rock':
        print("You win!!!!")
    elif player_play == 'rock' and cpu_play == 'lizard':
        print("You win!!!!")
    elif player_play == 'lizard' and cpu_play == 'spock':
        print("You win!!!!")
    elif player_play == 'spock' and cpu_play == 'scissors':
        print("You win!!!!")
    elif player_play == 'scissors' and cpu_play == 'lizard':
        print("You win!!!!")
    elif player_play == 'lizard' and cpu_play == 'paper':
        print("You win!!!!")
    elif player_play == 'paper' and cpu_play == 'spock':
        print("You win!!!!")
    elif player_play == 'spock' and cpu_play == 'rock':
        print("You win!!!!")
    elif player_play == 'rock' and cpu_play == 'scissors':
        print("You win!!!!")
    else:
        print("You lose.")

game()


