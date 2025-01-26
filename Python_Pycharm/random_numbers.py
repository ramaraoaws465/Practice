import random

#print(help(random))

low = 1
high = 100

options = ("Rock", "Paper", "Scissors")
cards = ["2","3", "4","5", "6", "7","8", "9", "10", "J", "Q", "K","A"]
#option = random.choice(options)
#number = random.randint(low, high)
#number = random.random()
#print(option)

random.shuffle(cards)
print(cards)