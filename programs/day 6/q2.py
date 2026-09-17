n = int(input("Enter a number: "))
count_prime=0
count_com=0
while n>0:
    num = n%10
    if num==2:
        count_prime+=1
    else:
        for i in range(2,num):
            if num%i==0:
                count_com+=1
                break
            elif num==2:
                count_prime+=1
            elif num%i!=0:
                count_prime+=1
                break
            else:
                continue
    n//=10
print(count_prime)
print(count_com)