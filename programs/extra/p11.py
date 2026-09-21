a = [2, 3, 4, 7, 11]
k = int(input("Enter kth positive to search: "))
last = a[-1]
count = 0
for i in range(1,last):
    if i in a:
        continue
    else:
        count+=1
        if count == k:
            ans = i
            break
print(ans)
        