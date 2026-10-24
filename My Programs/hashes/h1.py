n = int(input())
a = list(map(int, input().split()))
f7 = {}
for i in a:
    if i in f7:
        f7[i] +=1
    else:
        f7[i] = 1
for j in f7:
    print(f"{j} {f7[j]}")