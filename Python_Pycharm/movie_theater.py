
print("-----------------------------")
print("Welcome to AMC Movie Theater")
print("-----------------------------")

movie_entry_type = {"A", "U/A", "U"}
age = int(input("Enter your age : "))

if age >= 12:
    if  movie_entry_type == "U":
        print("You are allowed")
    elif movie_entry_type == "U/A":
        print("You are allowed under parent's supervision")
    elif movie_entry_type == "A":
        print("you are not allowed for this movie")
    else:
        print("Check your age")
elif age >= 21:
    print("You allowed for any movie type")



