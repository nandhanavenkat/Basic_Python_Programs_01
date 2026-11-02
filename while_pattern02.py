
# OUTPUT

"""
0 0 0 0 0 0 
0 1 1 1 1 0 
0 1 1 1 1 0 
0 1 1 1 1 0 
0 1 1 1 1 0 
0 0 0 0 0 0 

"""

a = 1

while a <= 6:
    
    b = 1
    
    while b <= 6:
        
        if a == 1 or a == 6 or b == 1 or b == 6:
            
            print("0", end = " ")
            
        else:
            
            print("1", end = " ")
            
        b += 1
        
    print()
    
    a += 1