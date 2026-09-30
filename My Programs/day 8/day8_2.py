"""A
          B B
       C C C
   D D D D
E E E E E
"""
n = int(input("enter range: "))
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n):
    for j in range(n-1,i,-1):
        print(" ",end=" ")
    
    for k in range(i+1):
        print(letter[i],end=" ")
    print()