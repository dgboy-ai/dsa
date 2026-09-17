x = int(input("Enter range: "))
if x<2:
    print('invalid')
else:
    for i in range(1,x+1):
        for j in range(2,i):
            if i%j==0:
                print(i)
                break
            else:
                continue