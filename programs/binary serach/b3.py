#First Occurance Finder
a = [2,4,6,6,6,7,7,7,8,8,8,9]
target = int(input("ENter element to search: "))
found= False
start = 0
end = len(a)-1

while start <= end:
    mid = start + (end-start)//2
    
    if a[mid]==target:
        found = True
        ans = mid
        end = end-1
    elif a[mid]> target:
        end = mid-1
    else:
        start = mid+1
if found:
    print(f"Element first found at {ans}")
else:
    print("Element not found")