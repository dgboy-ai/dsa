#Print Sum of square of first n natural number.
n = int(input("Enter n range: "))
sum=0
for i in range(n+1):
    sqr = i**2
    sum=sum+sqr
print(sum)