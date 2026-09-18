#Reverse number
n = int(input("Enter a Number: "))
c=n
reverse=0
while n>0:
    digit = n%10
    reverse=(reverse*10)+digit
    n//=10
if c==reverse:
    print(f" Palindrome Number: {reverse}")
else:
    print("Not")
