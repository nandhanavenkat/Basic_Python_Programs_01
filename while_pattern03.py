
# OUTPUT

"""
* * * * * 
*       * 
*       * 
*       * 
* * * * * 

"""

a = 1

while a <= 5:
    
    b = 1
    
    while b <= 5:
        
        if a == 1 or a == 5 or b == 1 or b == 5:
            
            print("*", end = " ")
            
        else:
            
            print(" ", end = " ")
            
        b += 1
        
    print()
    
    a += 1