
========================================================================================================
# Project 1
# Calculator
========================================================================================================
operator = input("Please enter addition, subtraction, multiplication, or division: ")

num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

if operator == "addition":
    result = num1 + num2
    print(f"The result of addition is: {result:.2f}")
elif operator == "subtraction":
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif operator == "multiplication":
    if num2 != 0:
        result = num1 * num2
        print(f"The result of multiplication is: {result:.2f}")
    else:
        print("Error: Multiplication by zero is not allowed.")
elif operator == "division":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result:.2f}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please enter addition, subtraction, multiplication, or division.")
  
========================================================================================================
# Project 2
# even-odd-checker
========================================================================================================
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
elif number % 2 != 0:
    print(f"{number} is odd.") 
else:
    print(f"{number} is neither even nor odd.")
========================================================================================================
# Project 3
# Number Guessing Game
========================================================================================================
import random
number = random.randint(1, 100)
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if number > guess:
        print("Number is higher")
    elif number < guess:
        print("Number is lower")
    elif number == guess:
         print("You guessed it!")
========================================================================================================
# Project 4
# to-do-list 
========================================================================================================





