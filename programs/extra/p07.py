#Find Second Largest Distinct Element

a = [2,4, 7, 2, 9, 7,9, 5,10]

large1 = a[0]
large2 = a[1]

for i in a:
    
    if i > large1:
        
        large2 = large1
        large1 = i
    
    elif i > large2 and i < large1:
        
        large2 = i
        
    else:
        continue
    
print(large2)
print(large1)

