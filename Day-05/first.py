import sys

def addition(num1, num2):
    add = num1 + num2
    return add

def subtraction(num1, num2):  
    sub = num1 - num2
    return sub

def multiplication(num1, num2):
    mul = num1 * num2
    return mul

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "addition":
    output = addition(num1, num2)  
    print(output)

if operation == "subtraction":
    output = subtraction(num1, num2)
    print(output)

if operation == "multiplication":
    output = multiplication(num1, num2)
    print(output)
