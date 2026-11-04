# functions with argument and with return type

"""
def multi(a,b):
    return a*b
result = multi(5,4)
print(result)
"""
"""
def s(a=6, b=6):
    return a + b
print(s())
"""

# functions with arguments and without return type

"""
def add(a,b):
    print(a+b)
add(10,20)
"""

# calculator - without argument and without return type

"""
def calculator():
    x = int(input("Enter X value : "))
    y = int(input("Enter Y value : "))
    op = input("Enter your Operator : ")
    if op == "+":
        print(x+y)
    elif op == "-":
        print(x-y)
    elif op == "*":
        print(x*y)
    elif op == "/":
        print(x/y)
    elif op == "//":
        print(x//y)
    elif op == "%":
        print(x%y)
    elif op == "**":
        print(x**y)
    else:
        print("Invalid Input")  
calculator()
"""

# calculator - with argument and without return type

"""
def calculator(a,b,c):
    if op == "+":
        print(x+y)
    elif op == "-":
        print(x-y)
    elif op == "*":
        print(x*y)
    elif op == "/":
        print(x/y)
    elif op == "//":
        print(x//y)
    elif op == "%":
        print(x%y)
    elif op == "**":
        print(x**y)
    else:
        print("Invalid Input")
x = int(input("Enter X value : "))
y = int(input("Enter Y value : "))
op = input("Enter your Operator : ")
calculator(x,y,op)
"""

# calculator - with argument and with return type

"""
def calculator(a,b,c):
    if op == "+":
        return print(x+y)
    elif op == "-":
        return print(x-y)
    elif op == "*":
        return print(x*y)
    elif op == "/":
        return print(x/y)
    elif op == "//":
        return print(x//y)
    elif op == "%":
        return print(x%y)
    elif op == "**":
        return print(x**y)
    else:
        return print("Invalid Input")
x = int(input("Enter X value : "))
y = int(input("Enter Y value : "))
op = input("Enter your Operator : ")
calculator(x,y,op)
"""


# Palindrome

"""
def palindrome(n):
    num1 = num
    num2 = 0
    for i in range (len(str(num))):
        a = num1%10
        num1 = num1//10
        num2 = num2*10+a
    if(num == num2):
        print("Palindrome")
    else:
        print("Not a Palindrome")

num = int(input("Enter a number : "))
palindrome(num)
"""
"""  
# Factorial

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
print(factorial(6))
"""
"""
# recursive

def table(n,i):
    if i > 10:
        return
    print(n, "x", i, "=", n*i)
    table(n,i+1)
table(5,1)

"""
"""
def isprime(n):

    if n < 2:

        return False

    for i in range(2, n):

        if n % i == 0:

            return False

    return True

print(isprime(7))"""

def display(i):

    if i > 5:

        return

    print(i)

    display(i + 1)

display(1)











    
