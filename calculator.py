try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    op = input("Enter operation (+, -, *, /): ")

    if op == "+":
        result = num1 + num2

    elif op == "-":
        result = num1 - num2

    elif op == "*":
        result = num1 * num2

    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            exit()
        result = num1 / num2

    else:
        print("Invalid operation")
        exit()

    print("Result =", result)

except ValueError:
    print("Please enter valid numbers")