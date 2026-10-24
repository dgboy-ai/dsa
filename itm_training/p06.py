# #K-th Missing Positive Number
# a = [2,3,4,7,11,12]
# c=a[-1] # last element value for loop vha tak chalega
# b = []
# k=int(input("Enter value of kth element to find: "))
# for i in range(1,c):
#     if i in a:
#         continue
#     else:
#         b.append(i)
# print(b[k-1])














a = [2,3,4,7,11,12]
k =int(input("Enter position"))
ma = a[-1]
count=0
for i in range(1,ma):
    if i not in set(a):
        count=count+1
        if k == count:
            print(i)
if k==0:
    print("No missing Values")



