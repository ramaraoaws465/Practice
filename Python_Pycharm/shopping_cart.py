## Shopping cart program


item = input("What item would you liek to buy? : ")
price = float(input("What is the price?: "))
quantity = int(input("How many you like ?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is : ${total}")

