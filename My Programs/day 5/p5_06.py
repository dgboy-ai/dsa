#Print Sum of cube of first n natural number
n = int(input("Enter n range: "))
sum=0
for i in range(n+1):
    sqr = i**3
    sum=sum+sqr
print(sum)