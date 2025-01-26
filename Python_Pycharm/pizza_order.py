print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you ant? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#How much they need to pay based on their size choice
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed wrong input size")

#How much to add their bill based on their pepperoni choice
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3

# How much they need to pay as final amount if they want extra cheese
if extra_cheese == "Y":
    bill += 1

print(f"your final bill is : ${bill}")
