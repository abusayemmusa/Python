cal = input("Enter the operation: add, sub, mul, div:").lower()
user = int(input("Enter the first number: "))
user2 = int(input("Enter the secend number: "))

if cal == "add":
  add = user + user2
  print(add)
if cal == "sub":
  sub = user - user2
  print(sub)
if cal == "mul":
  mul = user * user2
  print(mul)
if cal == "div":
  div = user / user2
  print(div)

