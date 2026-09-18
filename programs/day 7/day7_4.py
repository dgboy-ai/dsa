letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(4):
    num=0
    for j in range(4,i,-1):
        print(letter[num],end=" ")
        num+=1
    print()