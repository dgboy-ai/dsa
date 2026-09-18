""""A
    A B
    A B C
    A B C D
    A B C D E
"""
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(5):
    for j in range(i+1):
        print(letter[j],end=" ")
    print()