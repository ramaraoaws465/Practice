print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child Tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are  $7")
    else:
        bill = 12
        print("Adult tickets are $12")
    wants_photo = input("Do you want to have a photo on roller coaster? Type Y for Yes and N for No.")
    if wants_photo == "Y":
        #Add $3 to their bill
        bill += 3

    print(f"Your final bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")