import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

#TODO-1 - Create a place holder with the same number of blanks as the chosen word
placeholder = ""
word_length = len(chosen_word)
for position in range(1, 6):
    #print("this loop has run")
    placeholder += "_"
print(placeholder)
guess2 = input("Guess a letter : ").lower()

#TODO-2 - Create a "display that puts the guess letter in the right position and _ in the rest of the string
display = ""
for letter in chosen_word:
    if letter == guess2:
        display += letter
    else:
        display += "_"

print(display)

#TODO- Check if the user guesses(guess) is one of the letters in the choosen_word. Print "Right" if it
# is "Wrong"if it's not
