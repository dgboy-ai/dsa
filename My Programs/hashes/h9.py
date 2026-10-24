class Solution:
    def countOccurence(self,arr, k):
        dic = {}
        coun = 0
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for j in dic:
            if dic[j] > len(arr)//k:
                coun+=1
        return coun