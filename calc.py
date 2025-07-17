a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
option = input("Enter operation (+, -, *, /): ")
if option == '+':
    print(f"{a} + {b} = {a + b}")
elif option == '-':
    print(f"{a} - {b} = {a - b}")
elif option == '*': 
    print(f"{a} * {b} = {a * b}")
elif option == '/':
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("Error: Division by zero is not allowed you dumbass")
else:
    print("Error: Invalid operation. Please enter +, -, *, or /.")