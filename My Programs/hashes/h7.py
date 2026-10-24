n,m = map(int,input().split())
a = list(map(int,input().split()))
seen = {}
ans = []
for i in range(len(a)):
    sol = m - a[i]
    if sol in seen:
        ans.append(i)
        ans.append(seen[sol])
        break
    else:
        seen[a[i]] = i
        
if ans:
    print(*ans)
else:
    print(-1)