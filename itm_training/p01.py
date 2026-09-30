a = [10,3,5,9,2]
target = 8
found = False
arr = []

for i in range(len(a)):
    if not found:
        for j in range(i+1,len(a)):
            if a[i]+a[j]==target:
                arr.append(i)
                arr.append(j)
                found = True
                break
print(arr)