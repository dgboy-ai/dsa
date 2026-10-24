#Find Second Largest Distinct Element

a = [4,5]

if len(a)==2:
    large1 = a[0]
    large2 = a[1]

    if a[0]>a[1]:
        large1 = a[0]
    else:
        large2=large1
        large1=a[1]
        print(large2)
        print(large1)
        
elif len(a)<=1:
    print(-1)

else:
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

