from random import randint
from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

# Function to check the guessing answer with actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against and return number of turns remaining"""
    if user_guess > actual_answer:
        print("Number is too high!")
        return  turns - 1
    elif user_guess < actual_answer:
        print("Number is too low!")
        return turns - 1
    else:
        print(f"You got it! the answer was {actual_answer} ")

#Function o set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return  EASY_LEVEL_TURNS
    else:
       return  HARD_LEVEL_TURNS
def game():
    # Choosing a random number between 1 to 100
    print("Welcome to the number guessing game!")
    print(logo)
    print("I'm thinking of a number between 1 to 100.")
    answer = randint(1, 100)
    print(f"hurray, the answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to gues the answer")
        #Let the user guess the answer
        guess = int(input("Make a guess : "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you have run out of guesses, you lose")
            return
        elif guess != answer:
            print("Guess again. ")

game()
