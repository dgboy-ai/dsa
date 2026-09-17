a = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input("Enter Elements: "))
    a.append(element)

for i in range(1,len(a)):
    for j in range(i):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
        else:
            continue
print(a)        
    