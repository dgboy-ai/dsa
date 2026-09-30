"""         E
          E D
        E D C
      E D C B
    E D C B A
"""
n = int(input("enter range: "))
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n):
    num=n
    for j in range(n-1,i,-1):
        print(" ",end=" ")
    for k in range(i+1):
        print(letter[num-1],end=" ")
        num=num-1
    print()