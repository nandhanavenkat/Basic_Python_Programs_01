"""

n = "NANDHANA"
"""
"""
n = "SATHYA"
for i in n:
    for j in i:
        if i == 0 or j == 0:
            print(n[i], end = " ")
        else:
            print(" ",end=" ")
    print()
"""


# for loop
"""
n = "NANDHANA"
for i in range(8):
    for j in range(8):
        if i == 0:
            print(n[j], end=" ")
        elif i == 7:
            print(n[7-j], end=" ")
        elif j == 0:
            print(n[i], end=" ")
        elif j == 7:
            print(n[7-i], end=" ")
        else:
            print(" ", end=" ")
    print()
"""

# while loop

""""
n = "NANDHANA"
i = 0
while i < 8:
    j = 0
    while j < 8:
        if i == 0:
            print(n[j], end=" ")
        elif i == 7:
            print(n[i-j], end=" ")
        elif j == 0:
            print(n[i], end=" ")
        elif j == 7:
            print(n[j-i], end=" ")
        else:
            print(" ", end=" ")  
        j += 1 
    i += 1 
    print()

"""






























