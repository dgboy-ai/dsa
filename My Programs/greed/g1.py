a = list(map(int,input().split()))
b = list(map(int,input().split()))
count = 0
for i in range(len(a)):
    for j in range(len(b)):
        if b[j] >= a[i]:
            count+=1
            break
print(count)