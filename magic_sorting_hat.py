
G = 0
R = 0
H = 0
S = 0

print("Now, let's make a test to know wich house you will be placed!")
Q1 = int(input("Q1) Do you like Dawn or Dusk?\n 1) Dawn\n 2) Dusk\n"))

if Q1 == 1:
    G += 1
    R += 1
elif Q1 == 2:
    H += 1
    S += 1

else:
    print("Wrong input")

Q2 = int(input("Q2) When I’m dead, I want people to remember me as:\n1) The Good\n 2) The Great\n 3) The Wise\n 4) The Bold\n"))

if Q2 == 1:
    H += 1
elif Q2 == 2:
    S += 1
elif Q2 == 3:
    R += 1
elif Q2 == 4:
    G += 1
else:
    print("Wrong input")

Q3 = int(input("Q3) Which kind of instrument most pleases your ear?\n1) The violin\n 2) The trumpet\n 3) The piano\n 4) The drum\n"))

if Q3 == 1:
    S += 1
elif Q3 == 2:
    H += 1
elif Q3 == 3:
    R += 1
elif Q3 == 4:
    G += 1
else:
    print("Wrong input")

if G > max(R,H,S):
    print("Congrats!\n You're 🦁 Gryffindor")
elif R> max(G,H,S):
    print("Congrats!\n You're 🦅 Ravenclaw")
elif H> max(G,R,S):
    print("Congrats!\n You're 🦡 Hufflepuff")
elif S > max(G,H,R):
    print("Congrats!\n You're 🐍 Slytherin")
