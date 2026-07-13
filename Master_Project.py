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
