a = [3,5,6,7,2,11,8,9,10]
min = 9
max = a[0]
max2=a[1]
for i in a:
    if i > max:
        max2=max
        max = i
        
    elif i > max2 and i < max:
        max2=i
print(max)
print(max2)

for i in a:
    if i < min:
        min=i
print(min)