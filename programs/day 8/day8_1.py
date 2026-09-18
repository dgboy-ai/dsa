"""        1
         2 1
       3 2 1
     4 3 2 1
   5 4 3 2 1
"""
n = int(input("enter range: "))
for i in range(n):
    num=1+i
    for j in range(n-1,i,-1):
        print(" ",end=" ")
    
    for k in range(i+1):
        print(num,end=" ")
        num=num-1
    print()