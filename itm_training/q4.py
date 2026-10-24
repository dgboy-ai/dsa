# #Reverse number
n = int(input("Enter a Number: "))
# reverse=0
# while n>0:
#     digit = n%10
#     reverse=(reverse*10)+digit
#     n//=10
# print(f" Reverse of Number: {reverse}")

p=list(str(n))
ll = len(p)
l = 1
for i in range(len(p)//2):
    p[i],p[ll-l] = p[ll-l],p[i]
    l=l+1
print("".join(p))