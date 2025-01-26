#validatw username
#username must not contain more than 12 characters
#username must not contain spaces
#username must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
    print("Your user name can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"{username}")

