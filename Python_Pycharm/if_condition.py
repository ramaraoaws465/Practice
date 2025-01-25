
'''
age = int(input("Enter your age : "))
if age >= 100:
    print("You are too old to  signed up!")
elif age >= 18:
    print("You are now signed up for this program")
elif age < 0:
    print("You are not born yet!")
else:
    print("You must be 18+ to sign up for his program")  '''

response = input("Would you like food?(Y/N): ")
if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")