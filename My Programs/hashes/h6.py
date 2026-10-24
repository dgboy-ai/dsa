m,n = map(int,input().split())
a = list(map(int,input().split()))
seen = {}
ans = []
for i in range(len(a)):
    sol = n-a[i]
    if sol in seen:
        ans.append(seen[sol]+1)
        ans.append(i+1)
        break
    else:
        seen[a[i]] = i
if ans:
    print(*ans)
else:
    print(-1)