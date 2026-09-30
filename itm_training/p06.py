#K-th Missing Positive Number
a = [2,3,4,7,11,12]
c=a[-1] # last element value for loop vha tak chalega
b = []
k=int(input("Enter value of kth element to find: "))
for i in range(1,c):
    if i in a:
        continue
    else:
        b.append(i)
print(b[k-1])