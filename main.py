from replit import clear
from art import logo

print(logo)


#Addition
def add(n1, n2):
    return n1 + n2


#Subtract
def subtract(n1, n2):
    return n1 - n2


#Multiplication
def multiply(n1, n2):
    return n1 * n2


#Division
def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    num1 = float(input("what's the first number?:\t"))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation:")
        num2 = float(input("what's the next number?:\t"))
        function = operations[operation_symbol]
        answer = function(num1, num2)

        print(f"num1 {operation_symbol} num2 = {answer}")
        if input(
                f"Type 'y' to continue calculating with {answer},or type'n' to a new calculation:"
        ) == "y":
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()
