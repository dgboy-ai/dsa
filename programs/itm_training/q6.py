x=int(input("Enter Number: "))
count = 0
if x>0:
    while x>0:
        digit=x%10
        if digit == 7:
            count+=1
        x//=10
else:
    print("fake")
print(f"Count of Lucky 7 in {x} is {count}")