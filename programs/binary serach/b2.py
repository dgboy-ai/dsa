#Rotated sorted Array search
a = [6,7,8,9,10,3,4,5]
target=int(input("ENter element to find: "))
start = 0
found=False
end  = len(a)-1

while start<=end:
    mid = start + (end-start)//2
    
    if a[mid]==target:
        found=True
        break
    
    elif a[mid]>a[0]:
        if a[mid] > target and a[0] <= target:
            end=mid-1
        else:
            start = mid+1
            
    else:
        if a[mid]<target and a[0] > target:
            start = mid + 1
        else:
            end = mid -1
if found:
    print(f"Element found at {mid}")
else:
    print("Not found")
            
            
        