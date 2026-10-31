
# Count of how many even and odd numbers are present from 1 to 50

count_odd = 0

count_even = 0

for n in range(1,51):
    
    if(n%2 == 0):
        
        count_even += 1
        
    else:
        
        count_odd += 1
        
print("Total even numbers from 1 to 50 :",count_even)
    
print("Total odd numbers from 1 to 50 :",count_odd)
        
