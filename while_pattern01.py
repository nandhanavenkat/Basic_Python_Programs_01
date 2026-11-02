
# OUTPUT

"""

*       * 
  *   *   
    *     
  *   *   
*       * 

"""
a = 1

while a <= 5:
    
    b = 1
    
    while b <= 5:
        
        if a == b or a + b == 6:
            
            print("*", end = " ")
            
        else:
            
            print(" ", end = " ")
            
        b += 1
        
    print()
    
    a += 1