
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
# Student Grade System
========================================================================================================
print("===== Student Grade System =====")

name = input("Enter Student Name: ")
marks = float(input("Enter Marks (0-100): "))

if marks >= 80:
    grade = "A+"
elif marks >= 70:
    grade = "A"
elif marks >= 60:
    grade = "A-"
elif marks >= 50:
    grade = "B"
elif marks >= 40:
    grade = "C"
elif marks >= 33:
    grade = "D"
else:
    grade = "F"

print("\n----- Result -----")
print("Student Name:", name)
print("Marks:", marks)
print("Grade:", grade)

========================================================================================================
# Project 5
# to-do-list 
========================================================================================================
def main():
    tasks = []
    print("1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
    while True:   
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("add the task: ")
            tasks.append(task)
            print(f"-'{task}' added successfully!")
        elif choice == "2":
            if not tasks:
                print("No tasks in the list.")
            else:
                for task in tasks:
                    print(f"- {task}")
        elif choice == "3":
            if not tasks:
                print("No tasks to delete.")
            else:
                if task in tasks:
                     # tasks.remove(task)
                     task_name = input("Enter the task name to delete: ")
                     tasks.remove(task_name)
                    
        elif choice == "4":
            print("Exiting the program.")
            break
========================================================================================================
========================================================================================================

