
'''
for_sale = False

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")
'''
print("Welcome to the roller coaster")
height = int(input("What is your height in cm:  "))

if height >= 120:
    print("You can ride the rolercoaster ")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Pleae pay $5")
    elif age <= 18:
        print("Please pay $7 ")
    else:
        print("Please pay $12")
else:
    print("Sorry you have to grow taller before you can ride")