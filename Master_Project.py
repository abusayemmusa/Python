========================================================================================================
# project 1
# Calculetor Project
========================================================================================================

def add(num1, num2):
  return num1 + num2

def sub(num1, num2):
  return num1 - num2

def mul(num1, num2):
  return num1 * num2

def div(num1, num2):
   if num2 == 0:
      return "Cannot divide by zero"
   return num1 / num2

if __name__ == "__main__":
  num1 = int(input("Enter first number:"))
  num2 = int(input("Enter second number:"))
  condition = input("Enter add, sub, mul, div:").lower()
  if condition == "add":
     print(add(num1, num2))
  elif  condition == "sub":
     print("Result", sub(num1, num2))
  elif condition == "mul":
     print("Result", mul(num1, num2))
  elif  condition == "div":
     print("Result", div(num1, num2))
  else:
     print("Invalid input")

========================================================================================================
# Project 2
# even-odd-checker
========================================================================================================
def main():
  number = int(input("Enter a number: "))
  return number
if __name__ == "__main__":
  check = main()
  
  if check % 2 == 0:
    print("Number is even")
  else:
    print("Number is odd")
========================================================================================================
# Project 3
# Number Guessing Game
========================================================================================================
# Number Guessing Game
import random
def main():
  number = random.randint(1, 100)

  while True:
    choice = int(input("Guess the number: "))
    if choice == number:
      print("You guessed it!")
      break
    elif choice > number:
      print("Too high!")
    elif choice < number:
      print("Too low!")
if __name__ == "__main__":
    main()
  
========================================================================================================
# Project 4
# Student Grade System
========================================================================================================
def get_grade(marks):
    if marks >= 80:
        return "A+"
    elif marks >= 70:
        return "A"
    elif marks >= 60:
        return "A-"
    elif marks >= 50:
        return "B"
    elif marks >= 40:
        return "C"
    elif marks >= 33:
        return "D"
    else:
        return "F"


def display_result(name, marks):
    grade = get_grade(marks)

    print("\n===== Student Result =====")
    print("Student Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)


def main():
    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks (0-100): "))

    display_result(name, marks)


main()



========================================================================================================
========================================================================================================
========================================================================================================
========================================================================================================
========================================================================================================
========================================================================================================
========================================================================================================
========================================================================================================
========================================================================================================
========================================================================================================
========================================================================================================
========================================================================================================
