
# Building a Simple Calculator

num1 = float(input("Enter your first number:\n"))
op = input("Enter a number of operation:\n")
num2 = float(input("Enter your second number:\n"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Error 505")
    exit()
