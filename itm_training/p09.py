#binary search

a = [2, 5, 8, 12, 16, 23, 38, 45]
target = int(input("Enter target : "))
found = False
start = 0
end = len(a)-1

while start<=end:
    
    mid = start + (end - start)//2
    
    if a[mid]==target:
        found = True
        ans = mid
        break
    
    elif a[mid] > target:
        end = mid - 1 
        
    else:
        
        start = mid + 1
        
if found:
    print(f"target found and its index is {ans}")
else:
    print("Not found")