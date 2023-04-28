def add(n1, n2):

    return n1 + n2
def subtract(n1, n2):

    return n1 - n2

def multiply(n1, n2):

    return n1 * n2

def divide(n1, n2):
    return n1 / n2



def calculator():
    num1 = int(input("what is the first number"))
    for symbol in something:
       print(symbol)
    operation_symbol = input("pick an operations:")
    num2 = int(input("what is the second number:"))
    calculation_symbol = something[operation_symbol]
    print(calculation_symbol)
    answer = calculation_symbol(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input("type 'y' to continue calculating with {answer}, or type 'n' to start a h.:") == "y":
        calculator()


something = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
calculator()








