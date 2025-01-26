import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randmoly choose a word from the list, assign it to a variable a print it

random_num = random.choice(word_list)
print(random_num)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
guess1 = input("Guess the letter: ").lower()
print(guess1)

#TODO- Check if the user guesses(guess) is one of the letters in the choosen_word. Print "Right" if it
# is "Wrong"if it's not
for letter in random_num:
    if letter == guess1:
        print("Right")
    else:
        print("Wrong")

