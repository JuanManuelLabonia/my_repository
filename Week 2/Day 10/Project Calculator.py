from logo import logo

def add(n1, n2):
    return n1 + n2 
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
              "-": substract,
              "*": multiply,
              "/": divide}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for i in operations:
        print(i)
    keep_calculating = True

    while keep_calculating:
        keep_asking = True
        operation = input("Pick an operation: ")
        if operation not in operations:
            print ("You´ve entered an invalid operation")
            keep_calculating = False
        else:
            calculation_function = operations[operation]
            num2 = float(input("What's the next number?: "))
            answer = calculation_function(num1, num2) 
            print (f"{num1} {operation} {num2} = {answer}")
            while keep_asking:
                choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
                if choice == "y":
                    num1 = answer
                    keep_asking = False
                elif choice == "n":
                    calculator()
                    keep_asking = False
                else: 
                    print ("You´ve entered an invalid character. Please, try again.")

calculator()
                