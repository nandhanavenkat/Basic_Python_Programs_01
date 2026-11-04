
# Reverse a number using for and wile looping statement

a = int(input("Enter a number : "))

for i in range(len(str(a))):

    b = a % 10

    c = a // 10

    print(b, end = "")

    a = c



a = int(input("Enter a number : "))

while a > 0:

    b = a % 10

    c = a // 10

    print(b, end = "")

    a = c




