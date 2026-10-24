n,m = map(int,input().split())
a = set(map(int,input().split()))
b = set(map(int,input().split()))
c = []
for i in a:
    if i in b:
        c.append(i)
print(*c)