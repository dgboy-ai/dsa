# Two pointer Approch

a = [1,0,1,0,1,0,10]
start = 0
end = len(a)-1

for i in range(len(a)//2):
    if a[end]==0:
            start = start + 1
            end = end - 1
            continue
    elif a[start] == a[end]:
        start = start + 1
        end = end - 1
        continue
    elif a[start] == 0:
        a[start] , a[end] = a[end],a[start]
        start = start + 1 
        end = end - 1
    elif a[start]!=a[end]: 
        end = end - 1
        continue
print(a)

# Count Replacement approch
# a = [1,0,1,0,1,0]
# count0 = 0
# count1 = 0

# for i in a:
#     if i == 0:
#         count0+=1
#     else:
#         count1 += 1

# for i in range(0, count0):
#     a[i] = 0
    
# for j in range(count0,len(a)):
#     a[j]=1
    
# print(a)

# Sorting approch by selection sort (worst)

# a = [1,0,1,0,1,0]

# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i] > a[j]:
#             a[i] , a[j] = a[j],a[i]
            
#         elif a[i] <= a[j]:
#             continue
# print(a)

