a = [2,7,11,15,27]
target = int(input("Enter target"))
ans=[]
for i in range(len(a)):
    start = 0
    end = len(a)-1
    x = target
    while start <= end:
        
        mid = start + (end-start)//2
        
        if x == a[start]+a[end]:
            ans.append(start)
            ans.append(end)
        
        elif x > a[start]+a[end]:
            start = mid + 1
    
        else:
            end=mid-1
            
print(ans)
            
