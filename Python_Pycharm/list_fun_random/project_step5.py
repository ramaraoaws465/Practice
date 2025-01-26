import random

#TODO-1 -- Update the word list to use the word_list from handman_words.py
#import hangman_words
from hangman_words import word_list
#TODO-2 -- Update the code to use the stages from the file hangamn.py
#import hangman_art
from hangman_art import stages, logo
#TODO-3 - Import the logo from hangman_art.py and point at the start of the game
print(logo)

lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    #print("this loop has run")
    placeholder += "_"
print("Word to guess: " + placeholder)
game_over = False
correct_letters = []
while not game_over:
    # TODO-6 - Update the code to tell the user how many lives left
    print(f"**********************{lives}/6 LIVES LEFT***************************")
    guess = input("Guess a letter : ").lower()

# TODO-4 - If the user has entered a letter they've already guessed, print the letter and let them know
# we should not deduct a life for this Ex: You have laready guessed a
    if guess in correct_letters:
        print(f"You've have already guessed {guess}")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

#TODO-5 - if the letter is not in the chosen_word, print out the the letter and let them know it's not in the word.
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")

        if lives == 0:
            game_over = True
            #TODO - 7 Update the print statement below to give the user correct word they were trying to guess
            print(f"***********************IT WAS {chosen_word}!You lose*******************************")
        #print(lives)
    if "_" not in display:
        game_over = True
        print("You Win!")


#TODO-3 - Print the ASCII art from the list stages that corresponds to the
#  current number of lives the user has remaining

print(stages[lives])



