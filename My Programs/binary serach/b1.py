n = int(input("enter a Number: "))
a= [1, 2, 3, 5, 6, 7, 23, 23, 23, 37, 41, 42, 55, 225]
start = 0
found=False
end= len(a) - 1
while start <= end:
    mid = (start+end)//2
    if a[mid] == n:
        found=True
        break
    elif a[mid]>n:
        end=mid-1
    else:
        start=mid+1
if found:
    print(f"ELement found at {mid}")
else:
    print('Not found')