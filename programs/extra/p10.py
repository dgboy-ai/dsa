#Peak Index

a = [2, 4, 6, 8, 10, 8, 5]

start = 0
end = len(a)-1
found = False

while start <= end:
    
    mid = start + (end-start)//2
    
    if a[mid] > a[mid+1] and a[mid] > a[mid-1]:
        found = True
        ans = mid
        break
    
    elif a[mid] > a[mid-1] and a[mid] < a[mid+1]:
        start = mid + 1
        
    else:
        
        end = mid - 1
        
if found:
    print(f"Element Found at index {ans}")
else:
    print("Element Not found")