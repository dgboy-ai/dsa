n = int(input("enter a Number: "))
largest = 0
while n>0:
    digit = n%10
    if digit>largest:
        largest = digit
    n//=10
print(largest)