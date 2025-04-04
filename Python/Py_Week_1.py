# Simple Python program to perform a mathematical operation based on user input

# Asking the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Placeholder for the result
result = None

# Performing the operation based on user input
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operation"

# Printing the result
if isinstance(result, str):
    print(result)
else:
    print(f"{num1} {operation} {num2} = {result}")
