# print Sum of all digits, and without using sum() and str

# For using for loop

n = int(input("Enter a Value : "))

sum = 0

for i in range(len(str(n))):

    a = n % 10

    sum = sum + a

    b = n // 10

    n = b

print(sum)


# For using while loop

n = int(input("Enter a Value : "))

sum = 0

while n > 0:

    a = n % 10

    sum = sum + a

    b = n // 10

    n = b

print(sum)
