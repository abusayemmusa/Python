
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

if __name__ == "__main__":
    main()
========================================================================================================
# Project 6
# Temperature Converter
========================================================================================================
while True:
    choice = input("Choose an option (f)  (c)  (q): ").lower()
    if choice == "f":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")
    elif choice == "c":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C")
    elif choice == "q":
        print("Exiting the program.")
        break
========================================================================================================
# Project 7
# Password Generator Random
========================================================================================================
import random
import string
length = int(input("Enter your number of length: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(length))
print(password)
========================================================================================================
# Project 8
# simple quiz game dictionary
========================================================================================================
questions = (
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "What is the chemical symbol for gold?",
    "Who painted the Mona Lisa?",
    "What is the hardest natural substance on Earth?"
)
options = (
    ("A) London", "B) Berlin", "C) Paris", "D) Madrid"),
    ("A) Jupiter", "B) Saturn", "C) Mars", "D) Venus"),
    ("A) Ag", "B) Au", "C) Al", "D) Ar"),
    ("A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Michelangelo"),
    ("A) Diamond", "B) Graphite", "C) Platinum", "D) Iron")
)

answers = ("C", "A", "B", "C", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)

    for question_option in options[question_num]:
        print(question_option)

    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print(f"{answers[question_num]} is the correct answer.")

    question_num += 1

print("-------------------------")
print("RESULTS")
print("-------------------------")
print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score_percentage = int(score / len(questions) * 100)
print(f"Your score is: {score}/{len(questions)} ({score_percentage}%)")
========================================================================================================
# Project 9
# bmi calculator math python
========================================================================================================
# Project 10
========================================================================================================
# Project 11
# Simple ATM Machine
========================================================================================================
# Project 12
# Rock Paper Scissors
========================================================================================================
import random
options = ["rock", "paper", "scissors"]
computer = random.choice(options)

user = input("Enter rock, paper, or scissors: ").lower()
if user not in options:
    print("Invalid input. Please enter rock, paper, or scissors.")
elif user == computer:
    print(f"Both players selected {user}. It's a tie!")
elif user == "rock" and computer == "scissors":
    print("Rock smashes scissors! You win!")
elif user == "paper" and computer == "rock":
    print("Paper covers rock! You win!")
elif user == "scissors" and computer == "paper":
    print("Scissors cuts paper! You win!")
else:
    print(f"{computer.capitalize()} beats {user}! You lose.")
========================================================================================================
# Project 13
========================================================================================================
# Project 14
========================================================================================================
# Project 15
========================================================================================================
# Project 16
========================================================================================================
# Project 17
========================================================================================================
# Project 18
========================================================================================================
# Project 19
========================================================================================================
# Project 20
========================================================================================================
========================================================================================================
========================================================================================================
========================================================================================================
