# year = int(input("Ent er the year of your birth: "))
#
# if year > 1980 and year < 1994:
#     print("You are a millennial")
# elif year >= 1994:
#     print("You are a Gen Z")

try:
    age = int(input("How old are you? : "))
except ValueError:
    print("You have typed in invalid number, please Try again")
    age = int(input("How old are you? : "))

if age > 18:
    print(f"You can drive at age {age}")