from Python_Pycharm.python_quiz import answer


def add(n1, n2):
    return n1 + n2

#TODO: Write out the ther 3 functions -substarct, multiply and Divide

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#TODO: Add these 4 functions into a dictionary as the values, Keys - "+", "-", "*", "%"

operations = {
    "+" : add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#TODO: Use the dictionary operations to perform the calculations

#print(operations["*"](4, 8))
num1 = float(input("What is the first number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation: ")
num2 = float(input("What is the next number? : "))
# print(num1 + num2)
#answer1 = operations[operation_symbol](num1, num2)
#print(f"{num1} {operation_symbol} {num2} = {answer1}")