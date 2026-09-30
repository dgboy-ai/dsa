a = [3,5,6,7,2,11,8,9,10]

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] >= a[j]:
            a[i],a[j]=a[j],a[i]
print(a)