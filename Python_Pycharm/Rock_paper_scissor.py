import  random

options = ("rock", "paper", "scissors")
playing = True

while playing:

    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player : {player}")
    print(f"Computer:{computer}")

    if player == computer:
        print("It's a Tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    else:
        print("you lose!")

    if not input("Play again? (y/n): ").lower() == "y":
       playing = False

print("Thanks for Playing")