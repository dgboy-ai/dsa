a = [10,3,5,9,2]
target = 12
output_array=[]
found= False
for i in range(len(a)):
    if not found:
        element1 = a[i] 
        for j in range(i+1,len(a)):
            if a[i]+a[j]==target:
                output_array.append(i)
                output_array.append(j)
                found = True
                break
print(output_array)