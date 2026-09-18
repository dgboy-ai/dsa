"""    10
       10 11
       10 11 12
       10 11 12 13
       10 11 12 13 14
       10 11 12 13 14 15
"""
for i in range(6):
    num = 10
    for j in range(i+1):
        print(num,end=" ")
        num+=1
    print()