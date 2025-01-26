# nested loop = A loop with in the loop


rows = int(input("Enter the # of rows : "))
columns = int(input("Enter the # rows of columns : "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()