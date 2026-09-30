#Reverse number
n = int(input("Enter a Number: "))
reverse=0
while n>0:
    digit = n%10
    reverse=(reverse*10)+digit
    n//=10
print(f" Reverse of Number: {reverse}")