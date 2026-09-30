n = int(input())

arr = list(map(int, input().split()))

my_sum = 0

for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

count = 0
total = 0

for j in arr:
    total = total + j

for i in range(len(arr) - 1, 0, -1):
    count = count + 1
    my_sum = my_sum + arr[i]

    if my_sum > total / 2:
        break

print(count)