# f = {}
# f[1] = "one"
# f[2] = "two"
# f[3] = "three"
# print(f)
# print(f[1])
# print("Yes" if 1 in f else "No")

# f[2] = "TWO"

# arr = [1, 2, 1, 3, 2, 1]
# f7 = {}
# count = 0
# for i in arr:
#     if i in f7:
#         f7[i] +=1
#     else:
#         f7[i]=1
# print(f7)


arr = [4, 2, 4, 3, 2, 4, 2, 2]
f7 = {}
# largest = 0
for i in arr:
    if i in f7:
        f7[i] +=1
    else:
        f7[i]=1
l = []
for i in f7:
    l.append(f7[i])
print(l)

largest = 0
for i in l:
    if i>largest:
        largest = i
print(largest)

#character array - frequency ,  small ya large only