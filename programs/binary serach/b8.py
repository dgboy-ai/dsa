target = int(input("Enter No: "))
start = 0
found = False
a = [2,4,6,6,6,7,7,7,8,8,8,9]
end = len(a)-1

while start <= end:
    mid = start + (end - start)//2
    
    if a[mid]*a[mid] == target:
        ans=mid
        found = True
        break
    elif a[mid]*a[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
        
if found:
    print(f"Sqrt of {target} is found in array which is {ans}") 
else:
    print("Target Sqrt Not found in array")