#Print char from ‘Z’ to ‘A’ with the help of a for loop.
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(letter)-1,-1,-1):
    print(letter[i],end=" ")