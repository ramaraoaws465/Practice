#name = input("Enter your full name: ")
phone_number = input("Enter your phone number : ")
#result = len(name)
#result = name.find("a") # first occurance

#result  = name.rfind("q")
#name = name.capitalize() #capitalizes the first letter
#name = name.upper() #upper case of input
#@result = name.lower()
#result1 = name.isalpha()
#print(name)
#(result)
#print(result1)
#result = phone_number.count('-')
result = phone_number.replace("-", "")
print(result)

print(help(str))