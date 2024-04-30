def calculator():
    while True:
        print("Basic Arithmetic operations ") 
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Modulus")
        print("Enter any number where !(1-5) for Exit")
        operation = int(input("Enter operation in between(1-5): "))
        if operation not in range(1, 6):
            print("Exiting the calculator. Goodbye!")
            break
        try:
            num1 = float(input("Enter the First number: "))
            num2 = float(input("Enter the Second number: "))
        except ValueError:
            print("Invalid Input, Please enter valid number!")
            continue
        if operation == 1:
            result = num1 + num2
            print("Addition of values", num1, "+", num2, '=', result)
        elif operation == 2:
            result = num1 - num2
            print("Subtraction of values", num1, "-", num2, '=', result)
        elif operation == 3:
            result = num1 * num2
            print("Multiplication of values", num1, "*", num2, '=', result)
        elif operation == 4:
            result = division(num1, num2)
            print("Division of values", num1, "/", num2, '=', result)
        elif operation == 5:
            result = num1 % num2
            print("Modulus of values", num1, "%", num2, '=', result)
        else:
            print("Please enter valid number in range(1-6)")

def division(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please try again.")
        return None

calculator()