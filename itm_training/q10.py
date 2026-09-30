#codeforces 160A

n = int(input())
arr = list(map(int, input().split()))
sum = 0
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
        else:
            continue
count = 0
total = 0
print(arr)
for j in arr:
    total = total + j

for i in range(len(arr)-1,0,-1):
    count = count+1
    sum = sum + arr[i]
    if sum > total/2:
        break
print(count)