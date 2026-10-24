s = "geeksforgeeks"
dic = {}
for i in range(len(s)):
    if s[i] in dic:
        dic[s[i]]+=1
    else:
        dic[s[i]] = 1
print(dic)  
for j in dic:
    if dic[j] == 1:
        print(j)
        break
else:
    print('$')