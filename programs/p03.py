#Palindrome madam
#My own solve
a = "madamm"
num=1
count = 0
for i in range(len(a)//2):
    if a[i] == a[len(a)-num]:
        count +=1
    num=num+1
if count==(len(a)//2):
    print("Palindrome String")
else:
    print('Not Palindrome')    

## chatgpt hint for optimizing 
#Palindrome madam
a = "madam"
num=1
count = 0
palindrome = True
for i in range(len(a)//2):
    if a[i] == a[len(a)-num]:
        palindrome=True
    else:
        palindrome = False
        break
    num=num+1
if palindrome:
    print("Palindrome String")
else:
    print('Not Palindrome')