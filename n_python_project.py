========================================================================================================
# Project 1
# Hello World
========================================================================================================
name = input("What is your name? ")
print(f"Hello, {name}!")
print("Welcome to Python programming.")
========================================================================================================
# Project 2
# Calculator
========================================================================================================
condition = input("Enter the operation (add, sub, mul, div): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if condition == "add":
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}")
elif condition == "sub":
    result = num1 - num2
    print(f"The difference between {num1} and {num2} is {result}")
elif condition == "mul":
    result = num1 * num2
    print(f"The product of {num1} and {num2} is {result}")
elif condition == "div":
    if num2 != 0:
        result = num1 / num2
        print(f"The quotient of {num1} and {num2} is {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter add, sub, mul, or div.")
========================================================================================================
# Project 3
# Even/Odd Checker
========================================================================================================
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
========================================================================================================
# Project 4
# Prime Number Checker
========================================================================================================










