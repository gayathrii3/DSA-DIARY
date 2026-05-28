import random 

options = ("rock", "papaer", "scissor")

playing = True

while playing:
    player = input("Enter a choice(rock, papaer, scissor) : ")
    computer = random.choice(options)

    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == "rock" and computer == "scissor":
        print("You WIN!")
    elif player == "paper" and computer == "rock":
        print("You WIN!")
    elif player == "scissor" and computer == "paper":
        print("You WIN!")
    else:
        print("You LOSE!")

    if not input("Play again(y/n) : ").lower() == 'y':
        playing = False

print("Thanks for playing!")