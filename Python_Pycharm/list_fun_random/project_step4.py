import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel", "sidhiksha"]

#TODO-1 -- Create a variable called 'lives' to keep track of the number of lives left
# set lives to 6

lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    #print("this loop has run")
    placeholder += "_"
print(placeholder)
game_over = False
correct_letters = []
while not game_over:
    guess = input("Guess a letter : ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

#TODO-2 - If guess is not in a letter in the chosen word, Then reduce lives by 1
# if lives goes down to 0 then the game should end, and it should print "You lose"
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose")
        print(lives)
    if "_" not in display:
        game_over = True
        print("You Win!")


#TODO-3 - Print the ASCII art from the list stages that corresponds to the
#  current number of lives the user has remaining

print(stages[lives])



