#Reverse The array
a = [10,2,4,5,2,6,9]
b = len(a)
num = 1
for i in range(b//2):
    a[i],a[b-num] = a[b-num],a[i]
    num = num + 1
print(a)