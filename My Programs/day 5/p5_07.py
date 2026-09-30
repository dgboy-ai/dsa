#Print n’th Fibonacci number.
n = int(input('Enter nth Range: '))
sum = 0
print(0,end=" ")
print(1,end=" ")
for i in range(1,n+1):
    sum = sum+i+i-1
    print(sum,end=" ")
# print("\n")
print("\n""=========================")
print(f"fibonacci number of nth term is : {sum}")